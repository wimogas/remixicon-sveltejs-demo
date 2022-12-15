<script>
  import Tooltip from "./Tooltip.svelte";
  import Toast from "./Toast.svelte";
  export let items;
  let index;

  let toggleTooltipSwitch = false;
  let toggleCopyIndicator = false;

  const handleTooltip = (i, e) => {
    e.stopPropagation()
    toggleTooltipSwitch = !toggleTooltipSwitch;
    return index = i
  }

  const copyIconText = (title) => {
    navigator.clipboard.writeText(title);
    toggleCopyIndicator = true;
    setTimeout(() => {
      toggleCopyIndicator = false
    }, 1000)
  }
</script>

<style>
  .items {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 8px;
  }
  .item {
    border: 1px solid #ccc;
    padding: 12px;
    border-radius: 4px;
    position: relative;
    cursor: pointer;
  }
</style>

<div class="items">
  {#each items as item, i}
    <div class="item" 
      on:mouseenter={(e) => {handleTooltip(i, e)}} 
      on:focus={(e) => handleTooltip(i, e)} 
      on:mouseleave={(e) => handleTooltip(i, e)} 
      on:blur={(e) => handleTooltip(i, e)}
      on:click={() => copyIconText(item.title)}
      on:keydown={() => copyIconText(item.title)}
    >
      <svelte:component this={item.component} {...item} />
      {#if toggleTooltipSwitch && i === index}
        <Tooltip text={item.title} parentWidth={46} />
      {/if}
    </div>
  {/each}
</div>

{#if toggleCopyIndicator}
  <Toast text="Copied!" />
{/if}
