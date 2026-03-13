<script>
  import { currentUser, logout } from '../../stores/auth.js'
  import PqrModule from './PqrModule.svelte'
  import UsuariosModule from './UsuariosModule.svelte'
  import HomeModule from './HomeModule.svelte'

  let { page = $bindable('home') } = $props()

  let isAdmin = $derived($currentUser?.id_rol === 1)

  const navItems = [
    { id: 'home',     label: 'Inicio',   icon: '⊞', always: true },
    { id: 'pqrs',     label: 'PQRs',     icon: '◈', always: true },
    { id: 'usuarios', label: 'Usuarios', icon: '◉', admin: true  },
  ]

  function handleLogout() {
    logout()
  }
</script>

<div class="layout">
  <!-- SIDEBAR -->
  <aside class="sidebar">
    <div class="sidebar-top">
      <div class="brand">
        <div class="brand-icon">
          <svg width="28" height="28" viewBox="0 0 32 32" fill="none">
            <rect width="32" height="32" rx="8" fill="var(--accent)"/>
            <path d="M8 10h16M8 16h10M8 22h13" stroke="#0a0a0f" stroke-width="2.5" stroke-linecap="round"/>
          </svg>
        </div>
        <span class="brand-text">PQR Sistema</span>
      </div>

      <nav>
        {#each navItems as item}
          {#if item.always || (item.admin && isAdmin)}
            <button
              class="nav-item {page === item.id ? 'active' : ''}"
              onclick={() => page = item.id}
            >
              <span class="nav-icon">{item.icon}</span>
              <span>{item.label}</span>
            </button>
          {/if}
        {/each}
      </nav>
    </div>

    <div class="sidebar-bottom">
      <div class="user-card">
        <div class="avatar">{$currentUser?.nombre?.charAt(0)?.toUpperCase() || '?'}</div>
        <div class="user-info">
          <p class="user-name">{$currentUser?.nombre || 'Usuario'}</p>
          <p class="user-role">{$currentUser?.id_rol === 1 ? 'Administrador' : 'Usuario'}</p>
        </div>
      </div>
      <button class="btn-logout" onclick={handleLogout}>
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"/>
        </svg>
        Salir
      </button>
    </div>
  </aside>

  <!-- MAIN CONTENT -->
  <main class="main">
    {#if page === 'home'}
      <HomeModule onnavigate={(p) => page = p} />
    {:else if page === 'pqrs'}
      <PqrModule />
    {:else if page === 'usuarios' && isAdmin}
      <UsuariosModule />
    {:else}
      <div class="no-access">No tienes acceso a esta sección.</div>
    {/if}
  </main>
</div>

<style>
  .layout {
    display: flex;
    min-height: 100vh;
  }

  .sidebar {
    width: 240px;
    min-width: 240px;
    background: var(--surface);
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 24px 16px;
    position: sticky;
    top: 0;
    height: 100vh;
  }

  .brand {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 0 8px 28px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 20px;
  }

  .brand-text {
    font-family: var(--font-display);
    font-weight: 700;
    font-size: 16px;
    letter-spacing: -0.02em;
  }

  nav {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .nav-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 12px;
    border-radius: var(--radius-sm);
    border: none;
    background: transparent;
    color: var(--text-muted);
    font-size: 14px;
    font-weight: 500;
    transition: background 0.15s, color 0.15s;
    text-align: left;
    width: 100%;
  }

  .nav-item:hover {
    background: var(--surface2);
    color: var(--text);
  }

  .nav-item.active {
    background: rgba(45,45,58,0.08);
    color: var(--accent);
    border: 1px solid rgba(45,45,58,0.15);
  }

  .nav-icon { font-size: 16px; }

  .sidebar-bottom {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .user-card {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 12px;
    background: var(--surface2);
    border-radius: var(--radius-sm);
    border: 1px solid var(--border);
  }

  .avatar {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: var(--accent);
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-display);
    font-weight: 800;
    font-size: 16px;
    flex-shrink: 0;
  }

  .user-name {
    font-size: 13px;
    font-weight: 600;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .user-role {
    font-size: 11px;
    color: var(--text-muted);
  }

  .btn-logout {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 10px 12px;
    border-radius: var(--radius-sm);
    border: 1px solid var(--border);
    background: transparent;
    color: var(--text-muted);
    font-size: 13px;
    transition: all 0.15s;
    width: 100%;
  }

  .btn-logout:hover {
    background: rgba(255,71,71,0.1);
    border-color: rgba(255,71,71,0.3);
    color: var(--danger);
  }

  .main {
    flex: 1;
    overflow-y: auto;
    background: var(--bg);
  }

  .no-access {
    padding: 40px;
    color: var(--text-muted);
  }

  @media (max-width: 768px) {
    .layout { flex-direction: column; }
    .sidebar {
      width: 100%;
      height: auto;
      position: static;
      flex-direction: row;
      flex-wrap: wrap;
      padding: 16px;
      gap: 8px;
    }
    .sidebar-top { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; flex: 1; }
    .brand { border-bottom: none; padding-bottom: 0; margin-bottom: 0; }
    nav { flex-direction: row; }
    .sidebar-bottom { flex-direction: row; align-items: center; }
    .user-info { display: none; }
  }
</style>