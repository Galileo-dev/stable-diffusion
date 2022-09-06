<script>
  import { onMount } from "svelte";
  import ImagePrompt from "./components/ImagePrompt.svelte";
  import ImageUpload from "./components/ImageUpload.svelte";
  import ImageView from "./components/ImageView.svelte";
  import Nav from "./components/Nav.svelte";
  import ServerURl from "./components/ServerURl.svelte";
  import {} from "./api";
  import { IP } from "./store.js";
  onMount(async () => {
    fetch($IP + "/rand")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.log(error);
        return [];
      });
  });
</script>

<Nav />
<main>
  <div class="container">
    <ServerURl />

    <ImagePrompt />
    <ImageUpload />
    <ImageView />
  </div>
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  .container {
    max-width: calc(var(--content-large) + var(--content-h-padding) * 2);
    text-align: center;
    padding-top: 180px;
    padding: 1em;
    margin: 0 auto;
  }

  h1 {
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }
  main {
    max-width: none;
  }
</style>
