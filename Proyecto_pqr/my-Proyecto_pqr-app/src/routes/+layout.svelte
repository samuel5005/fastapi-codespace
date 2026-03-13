<script>
  import { currentUser } from '../stores/auth.js';
  import Login from '../lib/componentes/Login.svelte';
  import Dashboard from '../lib/componentes/Dashboard.svelte';

  let page = 'dashboard'

  function navigate(p) {
    page = p
  }
</script>

{#if $currentUser}
  <Dashboard bind:page />
{:else}
  <Login />
{/if}

<style>
  :global(*) {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  :global(:root) {
    --bg: #eef0f4;
    --surface: #ffffff;
    --surface2: #f5f6f9;
    --border: #dde0e8;
    --accent: #2d2d3a;
    --accent2: #4a6fa5;
    --danger: #d63031;
    --success: #00b894;
    --warning: #e17055;
    --text: #1a1a2e;
    --text-muted: #8890a0;
    --font-display: 'Syne', sans-serif;
    --font-body: 'DM Sans', sans-serif;
    --radius: 12px;
    --radius-sm: 8px;
    --shadow: 0 2px 16px rgba(0,0,0,0.07);
    --shadow-accent: 0 4px 24px rgba(45,45,58,0.12);
  }

  :global(body) {
    background: var(--bg);
    color: var(--text);
    font-family: var(--font-body);
    min-height: 100vh;
  }

  :global(button) {
    cursor: pointer;
    font-family: var(--font-body);
  }

  :global(input), :global(select), :global(textarea) {
    font-family: var(--font-body);
  }
</style>