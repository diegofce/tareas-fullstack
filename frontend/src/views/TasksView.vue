<template>
  <div class="tasks-container">
    <h1>Mis Tareas</h1>

    <!-- NUEVA TAREA -->
    <div class="new-task">
      <input v-model="form.title" placeholder="Título de la tarea..." class="input-new" />
      <input v-model="form.description" placeholder="Descripción (opcional)" class="input-new" />

      <button 
        @click="editingId ? updateTask() : createTask()" 
        class="btn-new primary"
      >
        {{ editingId ? "Guardar cambios" : "Agregar" }}
      </button>

      <button 
        v-if="editingId" 
        @click="cancelEdit" 
        class="btn-new secondary"
      >
        Cancelar
      </button>
    </div>

    <!-- FILTROS -->
    <div class="filters">
      <button :class="['filter-btn', { active: filter === 'all' }]" @click="filter = 'all'">Todas</button>
      <button :class="['filter-btn', { active: filter === 'pending' }]" @click="filter = 'pending'">Pendientes</button>
      <button :class="['filter-btn', { active: filter === 'completed' }]" @click="filter = 'completed'">Completadas</button>
    </div>

    <!-- LISTA -->
    <div v-if="loading" class="loading">Cargando tareas...</div>
    <ul v-else class="task-list">
      <li v-for="task in filteredTasks" :key="task.id" :class="{ done: task.completed }">
        <div class="task-info" @click="toggleComplete(task)">
          <span>{{ task.title }}</span>
          <small v-if="task.description"> — {{ task.description }}</small>
        </div>

        <div class="actions">
          <button @click.stop="startEdit(task)" class="edit-btn">✏️</button>
          <button @click.stop="deleteTask(task.id)" class="delete-btn">🗑</button>
          <button @click.stop="goToDetail(task)" class="detail-btn">Ver detalle</button>
        </div>
      </li>
    </ul>

    <button @click="logout" class="logout-btn">Cerrar sesión</button>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from "vue";
import api from "../api/axios";
import { useRouter, useRoute } from "vue-router";

const router = useRouter();
const route = useRoute();

const tasks = ref([]);
const filter = ref("all"); // all | pending | completed
const loading = ref(true);
const form = ref({ title: "", description: "" });
const editingId = ref(null);

// --- CARGAR TAREAS ---
const loadTasks = async () => {
  loading.value = true;
  try {
    const res = await api.get("/tasks/");
    tasks.value = res.data.map(t => ({
      ...t,
      completed: !!t.date_completed
    }));
  } catch (error) {
    console.error("Error al cargar tareas", error);
  }
  loading.value = false;
};

// --- FILTRO ---
const filteredTasks = computed(() => {
  if (filter.value === "completed") return tasks.value.filter(t => t.completed);
  if (filter.value === "pending") return tasks.value.filter(t => !t.completed);
  return tasks.value;
});

// --- CREAR ---
const createTask = async () => {
  try {
    const res = await api.post("/tasks/", form.value);
    tasks.value.push({ ...res.data, completed: !!res.data.date_completed });
    form.value = { title: "", description: "" };
  } catch (e) {
    console.error("Error al crear tarea", e);
  }
};

// --- EDITAR ---
const startEdit = (task) => {
  editingId.value = task.id;
  form.value = { title: task.title, description: task.description || "" };
};

const updateTask = async () => {
  try {
    const res = await api.patch(`/tasks/${editingId.value}/`, form.value);
    const idx = tasks.value.findIndex(t => t.id === editingId.value);
    tasks.value[idx] = { ...res.data, completed: !!res.data.date_completed };
    cancelEdit();
  } catch (e) {
    console.error("Error al actualizar tarea", e);
  }
};

const cancelEdit = () => {
  editingId.value = null;
  form.value = { title: "", description: "" };
};

// --- COMPLETAR / REABRIR ---
const toggleComplete = async (task) => {
  try {
    const newDate = task.completed ? null : new Date().toISOString();
    const res = await api.patch(`/tasks/${task.id}/`, { date_completed: newDate });
    const idx = tasks.value.findIndex(t => t.id === task.id);
    tasks.value[idx] = { ...res.data, completed: !!res.data.date_completed };
  } catch (e) {
    console.error("Error al cambiar estado de tarea", e);
  }
};

// --- ELIMINAR ---
const deleteTask = async (id) => {
  try {
    await api.delete(`/tasks/${id}/`);
    tasks.value = tasks.value.filter((t) => t.id !== id);
  } catch (e) {
    console.error("Error al eliminar tarea", e);
  }
};

// --- DETALLE ---
const goToDetail = (task) => {
  router.push(`/tasks/${task.id}`);
};

// --- LOGOUT ---
const logout = () => {
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
  router.push("/login");
};

// --- SINCRONIZAR FILTRO DESDE URL ---
onMounted(() => {
  if (route.query.filter) {
    filter.value = route.query.filter;
  }
  loadTasks();
});

watch(
  () => route.query.filter,
  (newVal) => {
    if (newVal) filter.value = newVal;
  }
);
</script>

<style scoped>
.tasks-container { max-width: 800px; margin: 2rem auto; }
.new-task { margin-bottom: 20px; display: flex; gap: 10px; flex-wrap: wrap; }

/* --------------------------------------------- */
/*              NUEVA TAREA (MEJORADO)           */
/* --------------------------------------------- */

.input-new {
  flex: 1 1 250px;
  padding: 10px 14px;
  border-radius: 8px;
  border: 1px solid #d1d1d1;
  background: #fafafa;
  transition: 0.25s ease;
  font-size: 14px;
}

.input-new:focus {
  background: #fff;
  border-color: #1976d2;
  box-shadow: 0 0 5px rgba(25, 118, 210, .3);
  outline: none;
}

.btn-new {
  padding: 10px 18px;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.25s;
}

.btn-new.primary {
  background: #1976d2;
  color: white;
}

.btn-new.primary:hover {
  background: #1155a3;
}

.btn-new.secondary {
  background: #e0e0e0;
  color: #333;
}

.btn-new.secondary:hover {
  background: #cacaca;
}

/* --------------------------------------------- */
/*          TODO LO DEMÁS ES TU CSS ORIGINAL     */
/* --------------------------------------------- */

.filters {
  margin: 20px 0;
  display: flex;
  gap: 12px;
  justify-content: center;
}

.filter-btn {
  padding: 8px 16px;
  border-radius: 20px;
  border: 1px solid #ccc;
  background: #f5f5f5;
  color: #333;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.filter-btn:hover {
  background: #e0e0e0;
}

.filter-btn.active {
  background: #1976d2;
  color: #fff;
  border-color: #1976d2;
  box-shadow: 0 2px 6px rgba(25, 118, 210, 0.4);
}

.task-list { list-style: none; padding: 0; }
.task-list li { display: flex; justify-content: space-between; align-items: center; padding: 10px; border-bottom: 1px solid #eee; }
.task-info { flex: 1; cursor: pointer; }
.actions { display: flex; gap: 8px; }
.done .task-info span { text-decoration: line-through; color: #888; }

.logout-btn {
  margin-top: 20px;
  background: #c62828;
  color: #fff;
  border: none;
  padding: 8px 12px;
  border-radius: 6px;
  cursor: pointer;
}

.edit-btn, .delete-btn, .detail-btn {
  background: #1976d2;
  color: #fff;
  border: none;
  padding: 6px 10px;
  border-radius: 4px;
  cursor: pointer;
}

.delete-btn { background: #c62828; }
.detail-btn { background: #43a047; }
</style>

