// Cambia esta URL si tu API corre en otro puerto o dominio
const API = "https://curly-space-parakeet-x5x9q6wg547qcv44g-8000.app.github.dev"

// ── USUARIOS ──────────────────────────────────────────────
export async function getUsuarios() {
  const res = await fetch(`${API}/get_usuarios/`)
  return res.json()
}

export async function getUsuario(id) {
  const res = await fetch(`${API}/get_usuario/${id}`)
  return res.json()
}

export async function createUsuario(data) {
  const res = await fetch(`${API}/create_usuario`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  return res.json()
}

export async function updateUsuario(id, data) {
  const res = await fetch(`${API}/update_usuario/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  return res.json()
}

export async function deleteUsuario(id) {
  const res = await fetch(`${API}/delete_usuario/${id}`, { method: 'DELETE' })
  return res.json()
}

export async function getUsuariosByRol(rolId) {
  const res = await fetch(`${API}/get_usuarios_by_rol/${rolId}`)
  return res.json()
}

// ── PQRs ──────────────────────────────────────────────────
export async function getPqrs() {
  const res = await fetch(`${API}/get_pqrs/`)
  return res.json()
}

export async function getPqr(id) {
  const res = await fetch(`${API}/get_pqr/${id}`)
  return res.json()
}

export async function createPqr(data) {
  const res = await fetch(`${API}/create_pqr`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  return res.json()
}

export async function updatePqr(id, data) {
  const res = await fetch(`${API}/update_pqr/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  return res.json()
}

export async function deletePqr(id) {
  const res = await fetch(`${API}/delete_pqr/${id}`, { method: 'DELETE' })
  return res.json()
}

export async function getPqrsByUsuario(usuarioId) {
  const res = await fetch(`${API}/get_pqrs_by_usuario/${usuarioId}`)
  return res.json()
}

export async function getPqrsByEstado(estadoId) {
  const res = await fetch(`${API}/get_pqrs_by_estado/${estadoId}`)
  return res.json()
}

export async function updateEstadoPqr(pqrId, nuevoEstadoId) {
  const res = await fetch(`${API}/update_estado_pqr/${pqrId}/${nuevoEstadoId}`, { method: 'PATCH' })
  return res.json()
}

export async function getPqrsByDepartamento(depId) {
  const res = await fetch(`${API}/get_pqrs_by_departamento/${depId}`)
  return res.json()
}

export async function getPqrsByPrioridad(prioridadId) {
  const res = await fetch(`${API}/get_pqrs_by_prioridad/${prioridadId}`)
  return res.json()
}

// ── RESPUESTAS ────────────────────────────────────────────
export async function getRespuestas() {
  const res = await fetch(`${API}/get_respuestas/`)
  return res.json()
}

export async function createRespuesta(data) {
  const res = await fetch(`${API}/create_respuesta`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  return res.json()
}

export async function getRespuestasByPqr(pqrId) {
  const res = await fetch(`${API}/get_respuestas_by_pqr/${pqrId}`)
  return res.json()
}

export async function getRespuestasByUsuario(usuarioId) {
  const res = await fetch(`${API}/get_respuestas_by_usuario/${usuarioId}`)
  return res.json()
}

// ── EVIDENCIAS ────────────────────────────────────────────
export async function getEvidenciasByPqr(pqrId) {
  const res = await fetch(`${API}/get_evidencias_by_pqr/${pqrId}`)
  return res.json()
}

export async function createEvidencia(data) {
  const res = await fetch(`${API}/create_evidencia`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  return res.json()
}

// ── CATÁLOGOS ─────────────────────────────────────────────
export async function getEstados() {
  const res = await fetch(`${API}/get_estados/`)
  return res.json()
}

export async function getDepartamentos() {
    const res = await fetch(`${API}/get_departamentos/`);
    const data = await res.json();
    return data.resultado; // <--- Importante: añadir .resultado
}

export async function getPrioridades() {
    const res = await fetch(`${API}/get_prioridades/`);
    const data = await res.json();
    return data.resultado; // <--- Importante: añadir .resultado
}

export async function getTiposPqr() {
    const res = await fetch(`${API}/get_tipo_pqrs/`);
    const data = await res.json();
    return data.resultado; // <--- AGREGA EL .resultado AQUÍ

}

export async function getRoles() {
  const res = await fetch(`${API}/get_rols/`)
  return res.json()
}

// ── ESTADÍSTICAS PARA DASHBOARD ───────────────────────────
export async function getConteoPqrsPorEstado() {
  const res = await fetch(`${API}/get_conteo_pqrs_por_estado/`)
  return res.json()
}

export async function getConteoPqrsPorDepartamento() {
  const res = await fetch(`${API}/get_conteo_pqrs_por_departamento/`)
  return res.json()
}

export async function getConteoPqrsPorTipo() {
  const res = await fetch(`${API}/get_conteo_pqrs_por_tipo/`)
  return res.json()
}

// ── ASIGNACIONES ──────────────────────────────────────────
export async function getAsignacionByPqr(pqrId) {
  const res = await fetch(`${API}/get_asignacion_by_pqr/${pqrId}`)
  return res.json()
}

export async function getAsignacionesByUsuario(usuarioId) {
  const res = await fetch(`${API}/get_asignaciones_by_usuario/${usuarioId}`)
  return res.json()
}

export async function createAsignacion(data) {
  const res = await fetch(`${API}/create_asignacion_responsable`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  return res.json()
}

// ── HISTORIAL ─────────────────────────────────────────────
export async function getHistorialByPqr(pqrId) {
  const res = await fetch(`${API}/get_historial_by_pqr/${pqrId}`)
  return res.json()
}

// ── EXPORT OBJETO api ─────────────────────────────────────
export const api = {
  // Usuarios
  getUsuarios, getUsuario, createUsuario, updateUsuario, deleteUsuario, getUsuariosByRol,
  // PQRs
  getPqrs, getPqr, createPqr, updatePqr, deletePqr,
  getPqrsByUsuario, getPqrsByEstado, updateEstadoPqr,
  getPqrsByDepartamento, getPqrsByPrioridad,
  // Respuestas
  getRespuestas, createRespuesta, getRespuestasByPqr, getRespuestasByUsuario,
  // Evidencias
  getEvidenciasByPqr, createEvidencia,
  // Catálogos
  getEstados, getDepartamentos, getPrioridades, getTiposPqr, getRoles,
  // Dashboard
  getConteoPqrsPorEstado, getConteoPqrsPorDepartamento, getConteoPqrsPorTipo,
  // Asignaciones
  getAsignacionByPqr, getAsignacionesByUsuario, createAsignacion,
  // Historial
  getHistorialByPqr
}