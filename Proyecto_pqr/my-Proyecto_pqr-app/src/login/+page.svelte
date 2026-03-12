<script>
	let correo = "";
	let password = "";
	let mensaje = "";

	async function iniciarSesion() {

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
	}
</script>

<h1>Login</h1>

<input 
	type="email" 
	placeholder="Correo"
	bind:value={correo}
/>

<input 
	type="password"
	placeholder="Contraseña"
	bind:value={password}
/>

<button on:click={iniciarSesion}>
	Iniciar sesión
</button>

<p>{mensaje}</p>
