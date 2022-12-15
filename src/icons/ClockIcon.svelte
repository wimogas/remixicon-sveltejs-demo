<script>
  import Icon from '../Icon.svelte';
  import svg from '../assets/svg-clean/Clock.svg?raw';
  export let size = '20px';
  export let color = '#2E383A';
</script>

<div style:width={size} style:height={size} style:color>
  <Icon data={svg} />
</div>
