<script>
  let fileinput;
</script>

<div>
  Or, <span
    class="file-link"
    on:click={() => {
      fileinput.click();
    }}>upload an image</span
  > to edit
</div>
<input
  type="file"
  accept="image/*"
  class="file-picker-input"
  style="display:none"
  bind:this={fileinput}
/>

<style>
  div {
    margin-top: 20px;
  }

  .file-link {
    font-weight: 500;
  }
</style>
