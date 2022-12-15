<script>
  export let text;
  export let parentWidth;
  let divWidth;
  let left;
  $: if (divWidth !== undefined) {
    left = `${(parentWidth / 2) - (divWidth / 2)}px`
  }
</script>

<style>
  .tooltip {
    position: absolute;
    background: black;
    color: white;
    padding: 12px;
    border-radius: 4px;
    z-index: 1000;
    display: flex;
    min-width: fit-content;
    white-space: nowrap;
    font-family: 'Source Code Pro';
    top: -115%;
  }

</style>

<div bind:offsetWidth={divWidth} class="tooltip" style:left>
  {text}
</div>
