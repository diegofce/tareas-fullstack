<template>
  <div class="detail-container" v-if="task">
    <h2>Detalle de tarea</h2>

    <p>
      <strong>Tarea creada por:</strong>
      {{ task.owner_username || task.user || task.owner }}
    </p>

    <label><strong>Título:</strong></label>
    <input v-model="task.title" />

    <label><strong>Descripción:</strong></label>
    <textarea v-model="task.description"></textarea>

    <p><strong>Estado:</strong> {{ task.completed ? "Completada" : "Pendiente" }}</p>

    <div class="actions">
      <button @click="updateTask">Actualizar</button>
      <button @click="toggleComplete">
        {{ task.completed ? "Reabrir" : "Finalizar tarea" }}
      </button>
      <button @click="deleteTask" class="danger">Eliminar</button>
      <button @click="goBack" class="secondary">Volver</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import api from "../api/axios";

const route = useRoute();
const router = useRouter();
const task = ref(null);

const loadTask = async () => {
  try {
    const res = await api.get(`/tasks/${route.params.id}/`);
    task.value = { ...res.data, completed: !!res.data.date_completed };
  } catch (err) {
    console.error(err);
  }
};

const updateTask = async () => {
  try {
    const res = await api.patch(`/tasks/${task.value.id}/`, {
      title: task.value.title,
      description: task.value.description,
    });
    task.value = { ...res.data, completed: !!res.data.date_completed };
  } catch (err) {
    console.error(err);
  }
};

const toggleComplete = async () => {
  try {
    const newDate = task.value.completed ? null : new Date().toISOString();
    const res = await api.patch(`/tasks/${task.value.id}/`, {
      date_completed: newDate,
    });
    task.value = { ...res.data, completed: !!res.data.date_completed };
  } catch (err) {
    console.error(err);
  }
};

const deleteTask = async () => {
  try {
    await api.delete(`/tasks/${task.value.id}/`);
    router.push("/tasks");
  } catch (err) {
    console.error(err);
  }
};

const goBack = () => router.back();

onMounted(loadTask);
</script>

<style scoped>
.detail-container {
  max-width: 700px;
  margin: 2rem auto;
  padding: 1rem;
  border: 1px solid #eee;
  border-radius: 8px;
}
label {
  display: block;
  margin-top: 10px;
}
input,
textarea {
  width: 100%;
  margin-top: 6px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 6px;
}
.actions {
  display: flex;
  gap: 8px;
  margin-top: 16px;
}
button {
  background: #1976d2;
  color: #fff;
  border: none;
  padding: 8px 12px;
  border-radius: 6px;
  cursor: pointer;
}
button.secondary {
  background: #888;
}
button.danger {
  background: #c62828;
}
</style>
