<script>
  import { onMount } from 'svelte'
  import { currentUser } from '../../stores/auth.js'
  import { api } from '../api.js'

  let pqrs = $state([])
  let loading = $state(true)
  let view = $state('list')
  let selected = $state(null)
  let saving = $state(false)
  let toastMsg = $state('')
  let toastType = $state('success')
  let searchText = $state('')
  let filterEstado = $state('')

  let tipos = $state([]), estados = $state([]), departamentos = $state([]), prioridades = $state([])

  let form = $state(defaultForm())

  function defaultForm() {
    return {
      descripcion: '',
      fecha: new Date().toISOString().slice(0,16),
      id_usuario: $currentUser?.id_usuario || 1,
      id_tipo: '',
      id_estado: 1,
      id_departamento: '',
      id_prioridad: ''
    }
  }

  let isAdmin = $derived($currentUser?.id_rol === 1)

  let filtered = $derived(pqrs.filter(p => {
    const matchText = !searchText || p.descripcion?.toLowerCase().includes(searchText.toLowerCase())
    const matchEstado = !filterEstado || p.id_estado == filterEstado
    return matchText && matchEstado
  }))

  onMount(async () => {
    await loadAll()
  })

  async function loadAll() {
    loading = true
    try {
      const [p, t, e, d, pr] = await Promise.allSettled([
        api.getPqrs(),
        api.getTiposPqr(),
        api.getEstados(),
        api.getDepartamentos(),
        api.getPrioridades(),
      ])
      pqrs = p.value?.resultado || []
      tipos = t.value?.resultado || []
      estados = e.value?.resultado || []
      departamentos = d.value?.resultado || []
      prioridades = pr.value?.resultado || []
    } catch(e) {}
    loading = false
  }

  function openCreate() {
    form = defaultForm()
    selected = null
    view = 'form'
  }

  function openEdit(pqr) {
    form = { ...pqr, fecha: pqr.fecha?.slice(0,16) }
    selected = pqr
    view = 'form'
  }

  function openDetail(pqr) {
    selected = pqr
    view = 'detail'
  }

  async function savePqr() {
    if (!form.descripcion || !form.id_tipo || !form.id_departamento || !form.id_prioridad) {
      showToast('Completa todos los campos requeridos', 'error')
      return
    }
    saving = true
    try {
      const payload = {
        ...form,
        fecha: new Date(form.fecha).toISOString(),
        id_usuario: form.id_usuario || $currentUser?.id_usuario || 1,
        id_tipo: parseInt(form.id_tipo),
        id_estado: parseInt(form.id_estado) || 1,
        id_departamento: parseInt(form.id_departamento),
        id_prioridad: parseInt(form.id_prioridad),
      }
      if (selected) {
        await api.updatePqr(selected.id_pqr, payload)
        showToast('PQR actualizada correctamente')
      } else {
        await api.createPqr(payload)
        showToast('PQR creada correctamente')
      }
      await loadAll()
      view = 'list'
    } catch(e) {
      showToast('Error al guardar: ' + e.message, 'error')
    }
    saving = false
  }

  async function deletePqr(id) {
    if (!confirm('¿Eliminar esta PQR?')) return
    try {
      await api.deletePqr(id)
      pqrs = pqrs.filter(p => p.id_pqr !== id)
      showToast('PQR eliminada')
      if (view === 'detail') view = 'list'
    } catch(e) {
      showToast('Error al eliminar', 'error')
    }
  }

  function showToast(msg, type = 'success') {
    toastMsg = msg
    toastType = type
    setTimeout(() => toastMsg = '', 3500)
  }

  function getLabelEstado(id) {
    const labels = ['','Pendiente','En proceso','Resuelto','Cerrado']
    return labels[id] || id
  }

  function getLabelTipo(id) {
    const t = tipos.find(t => t.id_tipo == id)
    return t?.nombre_tipo || id
  }

  function getLabelDep(id) {
    const d = departamentos.find(d => d.id_departamento == id)
    return d?.nombre_departamento || id
  }

  function getLabelPrio(id) {
    const p = prioridades.find(p => p.id_prioridad == id)
    return p?.nombre_prioridad || id
  }
</script>

<div class="module">
  {#if toastMsg}
    <div class="toast {toastType}" role="alert">{toastMsg}</div>
  {/if}

  <div class="page-header">
    <div>
      <h1>
        {#if view === 'list'}Gestión de PQRs
        {:else if view === 'form'}{selected ? 'Editar PQR' : 'Nueva PQR'}
        {:else}Detalle PQR
        {/if}
      </h1>
      <p class="subtitle">
        {#if view === 'list'}Peticiones, Quejas y Reclamos del sistema
        {:else if view === 'form'}Completa el formulario con la información requerida
        {:else}Información completa de la solicitud
        {/if}
      </p>
    </div>
    <div class="header-actions">
      {#if view !== 'list'}
        <button class="btn-secondary" onclick={() => view = 'list'}>← Volver</button>
      {/if}
      {#if view === 'list'}
        <button class="btn-primary" onclick={openCreate}>＋ Nueva PQR</button>
      {/if}
    </div>
  </div>

  {#if view === 'list'}
    <div class="toolbar">
      <div class="search-wrap">
        <svg class="search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
        <input class="search-input" type="text" placeholder="Buscar PQRs…" bind:value={searchText} />
      </div>
      <select class="filter-select" bind:value={filterEstado}>
        <option value="">Todos los estados</option>
        <option value="1">Pendiente</option>
        <option value="2">En proceso</option>
        <option value="3">Resuelto</option>
        <option value="4">Cerrado</option>
      </select>
    </div>

    {#if loading}
      <div class="loading-state">
        <span class="spinner-lg"></span>
        <p>Cargando PQRs…</p>
      </div>
    {:else if filtered.length === 0}
      <div class="empty-state">
        <div class="empty-icon">◈</div>
        <p>No hay PQRs {searchText ? 'que coincidan' : 'registradas'}</p>
        <button class="btn-primary" onclick={openCreate}>Crear primera PQR</button>
      </div>
    {:else}
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Descripción</th>
              <th>Tipo</th>
              <th>Departamento</th>
              <th>Prioridad</th>
              <th>Estado</th>
              <th>Fecha</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {#each filtered as pqr (pqr.id_pqr)}
              <tr onclick={() => openDetail(pqr)} class="clickable-row">
                <td><span class="id-badge">#{pqr.id_pqr}</span></td>
                <td class="desc-cell">{pqr.descripcion?.slice(0,50)}{pqr.descripcion?.length > 50 ? '…' : ''}</td>
                <td><span class="chip">{getLabelTipo(pqr.id_tipo)}</span></td>
                <td>{getLabelDep(pqr.id_departamento)}</td>
                <td><span class="prio p{pqr.id_prioridad}">{getLabelPrio(pqr.id_prioridad)}</span></td>
                <td><span class="status-badge s{pqr.id_estado}">{getLabelEstado(pqr.id_estado)}</span></td>
                <td class="date-cell">{pqr.fecha ? new Date(pqr.fecha).toLocaleDateString('es-CO') : '—'}</td>
                <td onclick={(e) => e.stopPropagation()}>
                  <div class="row-actions">
                    <button class="icon-btn edit" title="Editar" onclick={(e) => { e.stopPropagation(); openEdit(pqr) }}>✎</button>
                    {#if isAdmin}
                      <button class="icon-btn delete" title="Eliminar" onclick={(e) => { e.stopPropagation(); deletePqr(pqr.id_pqr) }}>✕</button>
                    {/if}
                  </div>
                </td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
      <p class="count-label">{filtered.length} de {pqrs.length} registros</p>
    {/if}

  {:else if view === 'form'}
    <div class="form-card">
      <div class="form-grid">
        <div class="field full">
          <label>Descripción <span class="req">*</span></label>
          <textarea bind:value={form.descripcion} rows="4" placeholder="Describe detalladamente tu petición, queja o reclamo…"></textarea>
        </div>

        <div class="field">
          <label>Tipo de PQR <span class="req">*</span></label>
          <select bind:value={form.id_tipo}>
            <option value="">Selecciona un tipo</option>
            {#each tipos as t}
              <option value={t.id_tipo}>{t.nombre_tipo}</option>
            {/each}
            {#if tipos.length === 0}
              <option value="1">Petición</option>
              <option value="2">Queja</option>
              <option value="3">Reclamo</option>
            {/if}
          </select>
        </div>

        <div class="field">
          <label>Departamento <span class="req">*</span></label>
          <select bind:value={form.id_departamento}>
            <option value="">Selecciona departamento</option>
            {#each departamentos as d}
              <option value={d.id_departamento}>{d.nombre_departamento}</option>
            {/each}
            {#if departamentos.length === 0}
              <option value="1">Sistemas</option>
              <option value="2">Administración</option>
              <option value="3">Académico</option>
            {/if}
          </select>
        </div>

        <div class="field">
          <label>Prioridad <span class="req">*</span></label>
          <select bind:value={form.id_prioridad}>
            <option value="">Selecciona prioridad</option>
            {#each prioridades as p}
              <option value={p.id_prioridad}>{p.nombre_prioridad}</option>
            {/each}
            {#if prioridades.length === 0}
              <option value="1">Baja</option>
              <option value="2">Media</option>
              <option value="3">Alta</option>
              <option value="4">Urgente</option>
            {/if}
          </select>
        </div>

        {#if isAdmin}
        <div class="field">
          <label>Estado</label>
          <select bind:value={form.id_estado}>
            {#each estados as e}
              <option value={e.id_estado}>{e.nombre_estado}</option>
            {/each}
            {#if estados.length === 0}
              <option value="1">Pendiente</option>
              <option value="2">En proceso</option>
              <option value="3">Resuelto</option>
              <option value="4">Cerrado</option>
            {/if}
          </select>
        </div>
        {/if}

        <div class="field">
          <label>Fecha</label>
          <input type="datetime-local" bind:value={form.fecha} />
        </div>
      </div>

      <div class="form-actions">
        <button class="btn-secondary" onclick={() => view = 'list'}>Cancelar</bu