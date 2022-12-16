<script>
  import Footer from './components/Footer.svelte';
  import * as Icons from './components/IconCategories/IconCategories'
  let selected = 'Buildings';
  let options = [];
  let color;
  let size;
  const keys = Object.keys(Icons)
  for (const key of keys) {
    options.push(key)
  }

</script>

<style>
  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 32px;
    padding: 32px 44px;
    margin-bottom: 70px;
  }

  h1 {
    margin: 0;
    font-family: 'Source Code Pro';
  }
  select {
    padding: 12px;
    border-radius: 4px;
    border: 1px solid #CCC;
    cursor: pointer;
    -webkit-appearance: none;
    -moz-appearance: none;
    background: transparent;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><g><path fill='none' d='M0 0h24v24H0z'/><path d='M12 15l-4.243-4.243 1.415-1.414L12 12.172l2.828-2.829 1.415 1.414z'/></g></svg>");
    background-repeat: no-repeat;
    background-size: 24px;
    background-position-x: 95%;
    background-position-y: 50%;
    min-width: 150px;
  }
</style>

<div class="container">
  <h1>Remixicon x Sveltejs</h1>
  <form>
    <select bind:value={selected}>
      {#each options as option}
        <option value={option}>{option}</option>
      {/each}
    </select>
  </form>
<svelte:component this={Icons[selected]}></svelte:component>
</div>
<Footer />

