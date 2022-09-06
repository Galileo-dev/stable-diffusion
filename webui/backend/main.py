from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
import random
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.state_holder = {}


@app.get("/rand")
async def hello():
    return random.randint(0, 100)


@app.get('/')
async def front():
    return hi
