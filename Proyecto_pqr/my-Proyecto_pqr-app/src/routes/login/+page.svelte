<script>
  let correo = "";
  let password = "";
  let mensaje = "";

  async function iniciarSesion() {
    mensaje = "Cargando...";
    
    try {
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
  
  <button on:click={iniciarSesion}>Entrar</button>
  
  {#if mensaje}
    <p>{mensaje}</p>
  {/if}
</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    max-width: 300px;
    gap: 10px;
    margin: 20px auto;
  }
</style>