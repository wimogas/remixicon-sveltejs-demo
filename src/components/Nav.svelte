<script>
    import DownloadIcon from "../icons/DownloadIcon.svelte";
</script>

<style>
    nav {
    height: 44px;
    background-color: black;
    padding: 12px 44px;
    color: white;
    display: flex;
    align-items: center;
    font-family: 'Source Code Pro';
    font-weight: bold;
    justify-content: space-between;
  }

  nav a {
    color: white;
    text-decoration: none;
  }

  .nav-right {
    display: flex;
    gap: 32px;
  }
</style>

<nav>
  <a href="/">BAREBONES</a>
  <div class="nav-right">
    <a href="https://github.com/wimogas/barebones-icons-sveltejs"><DownloadIcon color="white" /></a>
  </div>
</nav>