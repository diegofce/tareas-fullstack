import axios from "axios";

export const API_URL = import.meta.env.VITE_API_URL;

console.log("🌐 API_URL cargada:", API_URL); 
/* En el backend se usaria https://tareas-fullstack.onrender.com */


const api = axios.create({
  baseURL: API_URL,
});

// -------------------------------------------
// 🟢 ENDPOINTS QUE NO NECESITAN AUTENTICACIÓN
// -------------------------------------------
const noAuthRoutes = [
  "/token",
  "/token/",
  "/register",
  "/register/",
  "/users/register",
  "/users/register/",
];

// -------------------------------------------
// 🛡 INTERCEPTOR: AGREGA JWT AUTOMÁTICAMENTE
// -------------------------------------------
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access");
  const urlPath = config.url || "";

  // Detecta si la ruta necesita autenticación
  const requiresAuth = !noAuthRoutes.some((r) => urlPath.includes(r));

  if (requiresAuth && token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

export default api;
