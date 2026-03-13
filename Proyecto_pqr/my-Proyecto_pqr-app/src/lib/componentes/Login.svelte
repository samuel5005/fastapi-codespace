<script>
  import { currentUser } from '../../stores/auth.js'

  function loginAs(rol) {
    if (rol === 'admin') {
      currentUser.set({ nombre: 'Administrador', correo: 'admin@pqr.com', cedula: '123456', id_rol: 1 })
    } else {
      currentUser.set({ nombre: 'Juan Pérez', correo: 'user@pqr.com', cedula: '654321', id_rol: 2 })
    }
  }
</script>

<div class="login-bg">
  <div class="noise"></div>
  <div class="glow"></div>

  <div class="login-card">
    <div class="brand">
      <div class="brand-icon">
        <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
          <rect width="32" height="32" rx="8" fill="var(--accent)"/>
          <path d="M8 10h16M8 16h10M8 22h13" stroke="#0a0a0f" stroke-width="2.5" stroke-linecap="round"/>
        </svg>
      </div>
      <span class="brand-name">Sistema PQR</span>
    </div>

    <h1>Bienvenido</h1>
    <p class="subtitle">Selecciona tu tipo de acceso para continuar</p>

    <div class="roles-grid">
      <button class="role-card admin" onclick={() => loginAs('admin')}>
        <div class="role-icon">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
            <path d="M12 1l3 6.5L22 8.7l-5 4.9 1.2 7L12 17.2l-6.2 3.4L7 13.6 2 8.7l7-1.2z"/>
          </svg>
        </div>
        <div class="role-info">
          <span class="role-title">Administrador</span>
          <span class="role-desc">Acceso completo al sistema</span>
        </div>
        <span class="role-arrow">→</span>
      </button>

      <button class="role-card user" onclick={() => loginAs('usuario')}>
        <div class="role-icon">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
            <circle cx="12" cy="8" r="4"/>
            <path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/>
          </svg>
        </div>
        <div class="role-info">
          <span class="role-title">Usuario</span>
          <span class="role-desc">Gestión de PQRs propias</span>
        </div>
        <span class="role-arrow">→</span>
      </button>
    </div>
  </div>
</div>

<style>
  .login-bg {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--bg);
    position: relative;
    overflow: hidden;
  }

  .noise { display: none; }

  .glow {
    position: absolute;
    width: 700px;
    height: 700px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(45,45,58,0.04) 0%, transparent 70%);
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    pointer-events: none;
  }

  .login-card {
    position: relative;
    z-index: 1;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 48px 44px;
    width: 100%;
    max-width: 440px;
    box-shadow: var(--shadow);
    animation: fadeUp 0.5s ease;
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .brand {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 32px;
  }

  .brand-name {
    font-family: var(--font-display);
    font-weight: 700;
    font-size: 18px;
    letter-spacing: -0.02em;
  }

  h1 {
    font-family: var(--font-display);
    font-size: 32px;
    font-weight: 800;
    letter-spacing: -0.03em;
    line-height: 1.1;
    margin-bottom: 8px;
  }

  .subtitle {
    color: var(--text-muted);
    font-size: 14px;
    margin-bottom: 32px;
  }

  .roles-grid {
    display: flex;
    flex-direction: colu