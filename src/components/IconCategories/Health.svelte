<script>
  import IconList from "../../components/IconList.svelte";
  import * as Icons from 'remixicon-sveltejs/src/exports/health'
  export let filterIcon = '';
  let items = [];
  const keys = Object.keys(Icons)
  for (const key of keys) {
    items.push({ key, component : Icons[key], title: key })
  }
  if (filterIcon != '') {
    items = items.filter(item => item.key === filterIcon)
  }
</script>

<IconList {items} folder="health" />


