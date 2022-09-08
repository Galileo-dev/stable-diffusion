import { writable } from "svelte/store";
export const IP = writable("http://localhost:8000");
export const Session = writable();
