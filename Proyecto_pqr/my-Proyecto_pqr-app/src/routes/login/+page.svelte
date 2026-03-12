<script>
  // 1. En Svelte 5, usamos $state para que las variables sean reactivas
  let correo = $state("");
  let password = $state("");
  let mensaje = $state("");

  async function iniciarSesion() {
    mensaje = "Cargando...";
    
    try {
      // Recuerda cambiar localhost por la URL de Codespaces que vimos antes
      const respuesta = await fetch("http://localhost:8000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          correo: correo,
          password: password
        })
      });

      const data = await respuesta.json();
      mensaje = data.mensaje;

      if (data.usuario) {
        alert("Bienvenido");
      }
    } catch (error) {
      mensaje = "Error al conectar con el servidor";
      console.error(error);
    }
  }
</script>

<main>
  <h1>Iniciar Sesión</h1>
  
  <input type="email" bind:value={correo} placeholder="Correo">
  <input type="password" bind:value={password} placeholder="Contraseña">
  
  <button onclick={iniciarSesion}>Entrar</button>
  
  {#if mensaje}
    <p>{mensaje}</p>
  {/if}
</main>

<style>
  /* 1. Centrar todo en la pantalla */
  :global(body) {
    margin: 0;
    padding: 0;
    background-color: #f4f7f6; /* Un gris muy claro de fondo */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }

  /* 2. Caja del formulario */
  main {
    background: white;
    padding: 2.5rem;
    border-radius: 12px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1); /* Sombra suave */
    width: 100%;
    max-width: 350px;
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
  }

  h1 {
    margin: 0 0 0.5rem 0;
    color: #333;
    text-align: center;
    font-size: 1.8rem;
  }

  /* 3. Estilo de los inputs */
  input {
    padding: 12px;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 1rem;
    transition: border-color 0.3s;
  }

  input:focus {
    outline: none;
    border-color: #ff3e00; /* El naranja característico de Svelte */
  }

  /* 4. Estilo del botón */
  button {
    background-color: #ff3e00;
    color: white;
    padding: 12px;
    border: none;
    border-radius: 6px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: background 0.3s, transform 0.1s;
  }

  button:hover {
    background-color: #e63500;
  }

  button:active {
    transform: scale(0.98);
  }

  /* 5. Mensajes de error/estado */
  p {
    text-align: center;
    font-size: 0.9rem;
    color: #666;
    margin: 0;
    padding: 10px;
    background: #fff5f5;
    border-radius: 4px;
  }
</style>