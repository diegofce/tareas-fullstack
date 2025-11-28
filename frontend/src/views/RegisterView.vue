<template>
  <div class="auth-page">
    <h1>Registro</h1>

    <form @submit.prevent="register">
      <input v-model="username" placeholder="Usuario" required />
      <input v-model="password" type="password" placeholder="Contraseña" required />
      <button type="submit">Registrarse</button>
    </form>

    <p v-if="error" class="error">{{ error }}</p>
    <p v-if="success" class="success">{{ success }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import api from "../api/axios";
import { useRouter } from "vue-router";

const username = ref("");
const password = ref("");
const error = ref("");
const success = ref("");
const router = useRouter();

const register = async () => {
  error.value = "";
  success.value = "";

  try {
    // usamos la instancia api (baseURL ya contiene /api)
    const res = await api.post("/register/", {
      username: username.value,
      password: password.value
    });

    success.value = "Usuario creado. Redirigiendo a login...";
    // esperar un segundo para que el usuario lea el mensaje
    setTimeout(() => router.push("/login"), 1000);
  } catch (e) {
    console.error(e);
    // drf devuelve errores en e.response.data
    error.value = e.response?.data?.username || e.response?.data?.password || JSON.stringify(e.response?.data) || "Error en registro";
  }
};
</script>

<style scoped>
.auth-page { max-width:420px; margin:2rem auto; padding:16px; border:1px solid #eee; border-radius:6px; }
input { display:block; width:100%; margin:6px 0; padding:8px; }
button { padding:8px 12px; }
.error { color: #c00; margin-top:8px; }
.success { color: #080; margin-top:8px; }
</style>
