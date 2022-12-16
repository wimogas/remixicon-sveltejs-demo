<script>
  import Tooltip from "./Tooltip.svelte";
  import Toast from "./Toast.svelte";
  export let folder;
  export let items;
  let index;
  let iconName;

  let toggleTooltipSwitch = false;
  let toggleCopyIndicator = false;

  const handleTooltip = (i, e) => {
    e.stopPropagation()
    toggleTooltipSwitch = !toggleTooltipSwitch;
    return index = i
  }

  const copyIconText = (title) => {
    navigator.clipboard.writeText(`<${title} />`);
    toggleCopyIndicator = true;
    iconName = title;
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
  code {
    background-color: rgb(236, 236, 236);
    padding: 32px;
    border-radius: 4px;
    min-width: 550px;
    display: flex;
    justify-content: center;
  }
</style>
<code>
  import &#123; {iconName ? iconName : 'IconName'} &#125; from 'remixicon-sveltejs/src/exports/{folder}'
</code>
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
