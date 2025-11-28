<template>
  <nav class="navbar">
    <h2 class="logo">Tareas.com</h2>

    <ul class="nav-links">
      <!-- Siempre visible -->
      <li><router-link to="/">Home</router-link></li>

      <!-- Cuando NO hay sesión -->
      <template v-if="!isLoggedIn">
        <li><router-link to="/login">Login</router-link></li>
        <li><router-link to="/register">Register</router-link></li>
      </template>

      <!-- Cuando SÍ hay sesión -->
      <template v-else>
        <li class="welcome">Bienvenido, {{  }}</li>
      
        <li><button @click="logout" class="logout-btn">Cerrar sesión</button></li>
      </template>
    </ul>
  </nav>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const isLoggedIn = ref(false);
const username = ref("");

// --- Verificar sesión ---
const checkAuth = () => {
  const token = localStorage.getItem("access");
  isLoggedIn.value = !!token;

  // si guardas el usuario en localStorage al hacer login
  const storedUser = localStorage.getItem("username");
  username.value = storedUser || "Usuario";
};

onMounted(() => {
  checkAuth();
});

// actualizar estado al navegar
router.afterEach(() => {
  checkAuth();
});

// --- Logout ---
const logout = () => {
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
  localStorage.removeItem("username");
  isLoggedIn.value = false;
  username.value = "";
  router.push("/login");
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 20px;
  background: #282c34;
  color: white;
}

.logo {
  font-size: 20px;
  font-weight: bold;
}

.nav-links {
  display: flex;
  gap: 20px;
  list-style: none;
  align-items: center;
}

.nav-links a {
  color: white;
  text-decoration: none;
}

.welcome {
  font-style: italic;
  color: #ffd166;
}

.logout-btn {
  background: #e63946;
  border: none;
  padding: 6px 12px;
  color: white;
  cursor: pointer;
  border-radius: 5px;
}
</style>