<script>
  import { onMount } from 'svelte'
  import { currentUser } from '../../stores/auth.js'
  import { api } from '../api.js'

  let { onnavigate } = $props()

  let stats = $state({ pqrs: 0, usuarios: 0, pendientes: 0 })
  let recentPqrs = $state([])
  let loading = $state(true)

  let isAdmin = $derived($currentUser?.id_rol === 1)

  function getGreeting() {
    const h = new Date().getHours()
    if (h < 12) return 'Buenos días'
    if (h < 18) return 'Buenas tardes'
    return 'Buenas noches'
  }

  let greeting = $derived(getGreeting())

  onMount(async () => {
    try {
      const [pqrData, usrData] = await Promise.allSettled([
        api.getPqrs(),
        api.getUsuarios(),
      ])
      const pqrs = pqrData.value?.resultado || []
      const usuarios = usrData.value?.resultado || []
      stats.pqrs = pqrs.length
      stats.usuarios = usuarios.length
      stats.pendientes = pqrs.filter(p => p.id_estado === 1).length
      recentPqrs = pqrs.slice(0, 5)
    } catch(e) {}
    loading = false
  })
</script>

<div class="home">
  <header class="page-header">
    <div>
      <p class="greeting">{greeting},</p>
      <h1>{$currentUser?.nombre || 'Usuario'}</h1>
    </div>
    <div class="date-badge">
      {new Date().toLocaleDateString('es-CO', { weekday: 'long', day: 'numeric', month: 'long' })}
    </div>
  </header>

  <!-- STATS -->
  <div class="stats-grid">
    <div class="stat-card accent">
      <div class="stat-icon">◈</div>
      <div class="stat-num">{loading ? '…' : stats.pqrs}</div>
      <div class="stat-label">Total PQRs</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">⏳</div>
      <div class="stat-num">{loading ? '…' : stats.pendientes}</div>
      <div class="sta