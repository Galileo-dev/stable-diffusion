import os
import posixpath
from pydantic import BaseModel
from fastapi import HTTPException, FastAPI, Response, Depends, Request, WebSocket
from uuid import UUID, uuid4
from typing import List, Optional
import mimetypes
from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.session_verifier import SessionVerifier
from fastapi_sessions.frontends.implementations.cookie import SameSiteEnum
from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates

from fastapi.staticfiles import StaticFiles

mimetypes.init()


class CookieParameters(BaseModel):
    max_age: int = 14 * 24 * 60 * 60  # 14 days in seconds
    path: str = "/"
    domain: Optional[str] = None
    secure: bool = False
    httponly: bool = True
    samesite: SameSiteEnum = SameSiteEnum.lax

    class Config:
        use_enum_values = True
        validate_all = True


class SessionData(BaseModel):
    username: str


cookie_params = CookieParameters()

# Uses UUID
cookie = SessionCookie(
    cookie_name="cookie",
    identifier="general_verifier",
    auto_error=True,
    secret_key="DONOTUSE",
    cookie_params=cookie_params,
)
backend = InMemoryBackend[UUID, SessionData]()


class BasicVerifier(SessionVerifier[UUID, SessionData]):
    def __init__(
        self,
        *,
        identifier: str,
        auto_error: bool,
        backend: InMemoryBackend[UUID, SessionData],
        auth_http_exception: HTTPException,
    ):
        self._identifier = identifier
        self._auto_error = auto_error
        self._backend = backend
        self._auth_http_exception = auth_http_exception

    @property
    def identifier(self):
        return self._identifier

    @property
    def backend(self):
        return self._backend

    @property
    def auto_error(self):
        return self._auto_error

    @property
    def auth_http_exception(self):
        return self._auth_http_exception

    def verify_session(self, model: SessionData) -> bool:
        """If the session exists, it is valid"""
        return True


verifier = BasicVerifier(
    identifier="general_verifier",
    auto_error=True,
    backend=backend,
    auth_http_exception=HTTPException(
        status_code=403, detail="invalid session"),
)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/create_session/{name}")
async def create_session(name: str, response: Response):

    session = uuid4()
    data = SessionData(username=name)

    await backend.create(session, data)
    cookie.attach_to_response(response, session)

    return f"created session for {name}"


@app.get("/user")
@app.get("/user/")
def get_current_user(request: Request) -> Optional[str]:
    token = request.cookies.get("access-token")
    return 1


@app.get("/whoami", dependencies=[Depends(cookie)])
async def whoami(session_data: SessionData = Depends(verifier)):
    return session_data


@app.post("/delete_session")
async def del_session(response: Response, session_id: UUID = Depends(cookie)):
    await backend.delete(session_id)
    cookie.delete_from_response(response)
    return "deleted session"


@app.get("/static/{path:path}")
def static_resource(path: str):
    static_file = safe_join(os.path.join(
        os.getcwd(), '../frontend/public'), path)
    if static_file is not None:
        return FileResponse(static_file)
    raise HTTPException(status_code=404, detail="Static file not found")


templates = Jinja2Templates(directory="../frontend/public")


@app.head("/", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
def main(request: Request, user: str = Depends(get_current_user)):
    mimetypes.add_type("application/javascript", ".js")
    return templates.TemplateResponse("index.html", {"request": request, "id": id})


def safe_join(directory: str, path: str) -> Optional[str]:
    """Safely path to a base directory to avoid escaping the base directory.
    Borrowed from: werkzeug.security.safe_join"""
    _os_alt_seps: List[str] = list(
        sep for sep in [os.path.sep, os.path.altsep] if sep is not None and sep != "/"
    )

    if path != "":
        filename = posixpath.normpath(path)

    if (
        any(sep in filename for sep in _os_alt_seps)
        or os.path.isabs(filename)
        or filename == ".."
        or filename.startswith("../")
    ):
        return None
    return posixpath.join(directory, filename)
