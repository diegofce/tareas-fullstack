import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import TasksView from "../views/TasksView.vue";
import CompletedTaskView from "../views/CompletedTaskView.vue";


const routes = [
  { path: "/", component: HomeView },
  { path: "/login", component: LoginView },
  { path: "/register", component: RegisterView },
  { path: "/tasks", component: TasksView },
  { path: "/tasks/:id", component: () => import("../views/TaskDetailView.vue") },
  { path: "/tasks/date_completed", component: CompletedTaskView },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// -----------------------------
// 🔒 PROTECCIÓN DE RUTAS
// -----------------------------
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("access");

  // Rutas públicas (sin protección)
  const publicPages = ["/login", "/register"];

  // Se verifica usando startsWith para evitar errores con slashes
  const isPublic = publicPages.some(pub => to.path.startsWith(pub));

  // Si intenta acceder a una ruta protegida sin token → redirige
  if (!isPublic && !token) {
    return next("/login");
  }

  next();
});

export default router;
