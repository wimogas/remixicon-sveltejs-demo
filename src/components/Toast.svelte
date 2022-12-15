<script>
  export let text;
</script>

<style>
  .toast {
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
    bottom: 20px;
    left: 20px;
  }

</style>

<div class="toast" >
  {text}
</div>
