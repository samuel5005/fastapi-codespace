<script>
  import { onMount } from 'svelte'
  import { api } from '../api.js'

  let usuarios = $state([])
  let roles = $state([])
  let loading = $state(true)
  let view = $state('list')
  let selected = $state(null)
  let saving = $state(false)
  let toastMsg = $state('')
  let toastType = $state('success')
  let searchText = $state('')

  let form = $state(defaultForm())

  function defaultForm() {
    return {
      nombre: '', cedula: '', carrera: '',
      semestre: '', cargo: '', celular: '', correo: '', id_rol