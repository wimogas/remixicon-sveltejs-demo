<script>
  import Nav from './components/Nav.svelte'
  import IconList from "./components/IconList.svelte";
  import * as Icons from './icons'
  let items = [];
  const keys = Object.keys(Icons)
  for (const key of keys) {
    items.push({ component : Icons[key], title: `<${key} />` })
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
  }

  h1 {
    margin: 0;
    font-family: 'Source Code Pro';
  }

  table {
    max-width: 650px;
    background-color: rgb(243, 243, 243);
    padding: 18px;
    border-radius: 8px;
  }
  table th {
    text-align: left;
  }
  table td {
    border: 1px solid #ccc;
    width: 100%;
    padding: 12px;
  }
</style>
<Nav />
<div class="container">
  <h1>Icons</h1>
  <table>
    <tr>
      <th rows="2">Props:</th>
    </tr>
    <tr>
      <td>size</td>
      <td>"12px"</td>
    </tr>
    <tr>
      <td>color</td>
      <td>"red"</td>
    </tr>
  </table>
  <IconList {items} />
</div>

