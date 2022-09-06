<script>
  import { IP } from "../store";
</script>

<div>
  <p>Backend IP</p>
  <input type="text" name="server" bind:value={$IP} />
</div>

<style>
  p {
    text-align: left;
    margin: 0;
    font-size: 15px;
    letter-spacing: 0.75px;
    font-weight: 600;
  }

  div {
    position: absolute;
    right: 10px;
    top: 10px;
  }
</style>
