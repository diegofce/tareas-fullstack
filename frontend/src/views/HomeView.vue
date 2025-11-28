<template>
  <div class="home-container">
    <h1>Bienvenido a la Aplicación de Tareas</h1>
    <p class="subtitle">
      Gestiona tus pendientes de forma sencilla: crea, edita y completa tus tareas.
    </p>

    <div class="actions">
      <!-- Vista para invitados -->
      <template v-if="!auth">
        <router-link to="/login" class="btn primary">Iniciar sesión</router-link>
        <router-link to="/register" class="btn secondary">Registrarse</router-link>
      </template>

      <!-- Vista para usuarios logeados -->
      <template v-else>

        <router-link to="/tasks?filter=completed" class="btn secondary">Tareas completadas</router-link>
        <router-link to="/tasks?filter=pending" class="btn secondary">Tareas pendientes</router-link>
      </template>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";

const auth = computed(() => !!localStorage.getItem("access"));
</script>

<style scoped>
.home-container {
  max-width: 600px;
  margin: 3rem auto;
  text-align: center;
  padding: 2rem;
  border-radius: 12px;
  background: #f9f9f9;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.subtitle {
  margin: 1rem 0 2rem;
  font-size: 1.2rem;
  color: #555;
}

.actions {
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.btn {
  padding: 10px 18px;
  border-radius: 6px;
  text-decoration: none;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s;
}

.btn.primary {
  background: #1976d2;
  color: white;
}

.btn.primary:hover {
  background: #1565c0;
}

.btn.secondary {
  background: #43a047;
  color: white;
}

.btn.secondary:hover {
  background: #388e3c;
}
</style>