# Sally Icons (Sveltejs)
A pixel-perfect collection of custom-made icons to be used in all Sales Layer projects.

---

### 1. Installation
Install with npm:

```shell
npm install --save sally-icons
```

### 2. Usage
Import the icons you need into your Svelte project and use them in components:

```html
<script>
  import { AddIcon, CheckIcon } from 'sally-icons';
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
  import * as Icons from 'sally-icon';
</script>

<main>
  <Icon.CheckIcon />
</main>
```

## Author
Guillem Moya

## License
[MIT License](./LICENSE), Copyright © 2022-present.