<script>
  import { GithubFill } from 'remixicon-sveltejs/src/exports/logos'
</script>

<style>
  .footer {
    position: fixed;
    display: flex;
    justify-content: center;
    height: 60px;
    bottom: 0;
    width: 100%;
    align-items: center;
    background-color: black;
    color: white;
    z-index: 1001;
  }

  a {
    color: aqua;
    text-decoration: none;
    margin: 0 32px 0 4px;
  }

</style>

<footer class="footer">
  <GithubFill color="white"/> <a href="https://github.com/wimogas/remixicon-sveltejs" target="_blank" rel="noreferrer">remixicon-sveltejs</a> MIT License, Copyright © 2022-present. Guillem Moya.
</footer>
