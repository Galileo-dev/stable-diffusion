import { IP, Session } from "./store";
import { get } from "svelte/store";
const ENDPOINT = get(IP);

export async function auth() {
  await fetch(ENDPOINT + "/create_session/" + uuidv4(), {
    method: "POST",
    credentials: "same-origin",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      Session.set(data);
    })
    .catch((error) => {
      console.log(error);
      return [];
    });
}

function uuidv4() {
  return ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (
      c ^
      (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
    ).toString(16)
  );
}

export function generate_image(settings) {
  IP;
}
