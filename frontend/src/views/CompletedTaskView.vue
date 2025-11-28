<template>
  <div class="completed-container">
    <h1>Tareas Completadas</h1>

    <div v-if="loading" class="loading">Cargando tareas...</div>

    <ul v-else class="task-list">
      <li v-for="task in completedTasks" :key="task.id" class="task-item">
        <p><strong>Tarea creada por:</strong> {{ task.owner_username || task.owner }}</p>
        <h3>{{ task.title }}</h3>
        <p>{{ task.description }}</p>

        <div class="actions">
          <button @click="goToDetail(task.id)">Ver detalle</button>
          <button @click="reopenTask(task.id)">Reabrir</button>
          <button @click="deleteTask(task.id)" class="danger">Eliminar</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";
import api from "../api/axios";

const router = useRouter();
const tasks = ref([]);
const loading = ref(true);

// --- CARGAR TAREAS ---
const loadTasks = async () => {
  loading.value = true;
  try {
    const res = await api.get("/tasks/");
    // normalizamos completed según date_completed
    tasks.value = res.data.map(t => ({
      ...t,
      completed: !!t.date_completed
    }));
  } catch (err) {
    console.error("Error al cargar tareas", err);
  } finally {
    loading.value = false;
  }
};

// --- FILTRAR SOLO COMPLETADAS ---
const completedTasks = computed(() =>
  tasks.value.filter(t => t.completed)
);

// --- REABRIR TAREA ---
const reopenTask = async (id) => {
  try {
    const res = await api.patch(`/tasks/${id}/`, { date_completed: null });
    const idx = tasks.value.findIndex(t => t.id === id);
    tasks.value[idx] = { ...res.data, completed: !!res.data.date_completed };
  } catch (err) {
    console.error("Error al reabrir tarea", err);
  }
};

// --- ELIMINAR ---
const deleteTask = async (id) => {
  try {
    await api.delete(`/tasks/${id}/`);
    tasks.value = tasks.value.filter(t => t.id !== id);
  } catch (err) {
    console.error("Error al eliminar tarea", err);
  }
};

// --- DETALLE ---
const goToDetail = (id) => {
  router.push(`/tasks/${id}`);
};

onMounted(loadTasks);
</script>

<style scoped>
.completed-container { max-width: 800px; margin: 2rem auto; }
.task-list { list-style: none; padding: 0; }
.task-item { border: 1px solid #eee; padding: 12px; margin-bottom: 12px; border-radius: 6px; }
.actions { display: flex; gap: 8px; margin-top: 10px; }
button { background: #1976d2; color: #fff; border: none; padding: 6px 10px; border-radius: 4px; cursor: pointer; }
button:hover { opacity: 0.9; }
button.danger { background: #c62828; }
</style>