<script>
  // logic goes here
  function handleOnSubmit() {
    console.log("I'm the handleOnSubmit() in ImagePrompt.svelte");
  }

  let files;
</script>

<!-- markup (zero or more items) goes here -->
<form
  class="image-prompt-form desktop"
  on:submit|preventDefault={handleOnSubmit}
>
  <input
    type="text"
    class="text-input  text-input-medium text-input-outlined image-prompt-input"
    placeholder="An Impressionist oil painting of sunflowers in a purple vase…"
    maxlength="400"
    value=""
  />
  <button
    tabindex="0"
    class="btn btn-large btn-filled btn-secondary image-prompt-btn"
    type="submit"
    disabled=""
    aria-label="Submit prompt"
    ><span class="btn-label-wrap"
      ><span class="btn-label-inner">Generate‍</span></span
    ></button
  >
</form>

<style>
  .desktop .image-prompt-btn {
    align-items: center;
    background-color: var(--b0);
    border-left: 1px solid rgba(0, 0, 0, 0.05);
    display: flex;
    font-size: 16px;
    height: 100%;
    padding-left: 14px;
    padding-right: 16px;
  }

  .btn.btn-disabled-style {
    background-color: var(--b20);
    border-color: transparent;
    border-left-color: transparent;
    color: rgba(0, 0, 0, 0.5);
  }
  .btn-secondary.btn-filled,
  .btn-secondary.btn-filled:visited {
    color: var(--b100);
  }

  .btn-secondary.btn-filled {
    background-color: var(--b20);
  }
  .image-prompt-btn {
    border-radius: 0;
    cursor: pointer;
    transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out;
  }
  .btn-disabled {
    cursor: default;
    pointer-events: none;
  }
  .btn-filled,
  .btn-filled:visited {
    color: var(--b0);
  }
  .btn-large {
    font-size: 14px;
    line-height: 15px;
    padding: 17px 18px 16px;
    padding-right: 18px;
    padding-left: 18px;
  }
  .btn {
    border: none;
    border-top-color: currentcolor;
    border-right-color: currentcolor;
    border-bottom-color: currentcolor;
    border-left-color: currentcolor;
    border-left-style: none;
    border-left-width: medium;
    border-radius: 6px;
    border-radius: var(--btn-radius);
    box-sizing: border-box;
    cursor: pointer;
    display: inline-flex;
    font-weight: 700;
    justify-content: center;
    line-height: 1em;
    margin: 0;
    position: relative;
    text-decoration: none;
    transition: opacity 0.3s, box-shadow 0.3s, background-color 0.3s, color 0.3s;
    -webkit-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }
  button,
  textarea {
    font-family: ColfaxAI, Helvetica, sans-serif;
    font-family: var(--sans-serif);
  }

  .image-prompt-form {
    margin-top: 150px;
    background: var(--b0);
    border-radius: 6px;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 82, 0.15);
    overflow: hidden;
    transition: box-shadow 0.2s ease-in-out;
  }

  .image-prompt-form.desktop {
    align-items: center;
    display: flex;
    height: 44px;
    height: var(--page-background-color);
  }

  .image-prompt-input {
    border: none;
    flex: 1 1;
    height: 100%;
  }

  .text-input-outlined {
    border-radius: 6px;
    padding: 13px 14px;
  }

  .text-input:focus {
    outline: none;
  }

  .text-input {
    background-clip: padding-box;
    background-color: #fff;
    box-sizing: border-box;
    color: var(--b100);
    display: inline-block;
    font-family: var(--sans-serif);
    font-size: 15px;
    font-weight: 400;
    line-height: 1em;
    margin: 0;
    resize: none;
    vertical-align: top;
    width: 200px;
  }

  .image-prompt-form {
    background: var(--b0);
    border-radius: 6px;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 82, 0.15);
    overflow: hidden;
    transition: box-shadow 0.2s ease-in-out;
  }
  .image-prompt-form.desktop {
    align-items: center;
    display: flex;
    height: 44px;
    height: var(--image-prompt-input-height);
  }

  /* styles go here */
</style>
