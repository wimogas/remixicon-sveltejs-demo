# Barebones Icons (Sveltejs)
[DEMO](https://barebones-icons-sveltejs.vercel.app/)
A pixel-perfect collection of custom-made icons.

---

### 1. Installation
Install with npm:

```shell
npm install --save barebones-icons
```

### 2. Usage
Import the icons you need into your Svelte project and use them in components:

```html
<script>
  import { AddIcon, CheckIcon } from 'barebones-icons';
</script>

<main>
  <AddIcon />
  <CheckIcon />
</main>
```

Icons can be configured with inline props including inline ```style``` objects:

```html
<CheckIcon color="red" size="32px" />
```

You can also import the whole icon library:
```html
<script>
  import * as Icons from 'barebones-icon';
</script>

<main>
  <Icon.CheckIcon />
</main>
```

## Author
Guillem Moya

## License
[MIT License](./LICENSE), Copyright © 2022-present.