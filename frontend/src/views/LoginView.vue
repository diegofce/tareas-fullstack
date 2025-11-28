<template>
  <div class="auth-page">
    <h1>Iniciar sesión</h1>

    <form @submit.prevent="login">
      <input v-model="username" placeholder="Usuario" />
      <input v-model="password" type="password" placeholder="Contraseña" />
      <button type="submit">Entrar</button>
    </form>

    <p v-if="error" class="error">{{ error }}</p>

    <p>
      ¿No tienes cuenta?
      <router-link to="/register">Registrarse</router-link>
    </p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import api from "../api/axios";
import { useRouter } from "vue-router";
import { loginUser } from "../store/auth";

const username = ref("");
const password = ref("");
const error = ref("");
const router = useRouter();

const login = async () => {
  try {
    const res = await api.post("/token/", {
      username: username.value,
      password: password.value
    });

    loginUser(res.data.access, res.data.refresh);

    error.value = "";

    localStorage.setItem("access", res.data.access);
    localStorage.setItem("refresh", res.data.refresh);

    router.push("/tasks");
  } catch (err) {
    error.value = "Credenciales incorrectas";
  }
};
</script>

<style scoped>
.auth-page { max-width:420px; margin:2rem auto; padding:16px; border:1px solid #eee; border-radius:6px; }
input { display:block; width:100%; margin:6px 0; padding:8px; }
button { padding:8px 12px; }
.error { color:red; }
</style>
