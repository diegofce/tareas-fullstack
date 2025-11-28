<template>
  <Navbar />
  <router-view />
</template>

<script setup>
import Navbar from "./components/Navbar.vue";
</script>

<style>
/* Opcional: estilos globales */
body {
  font-family: Arial, sans-serif;
  margin: 20px;
}
</style>
