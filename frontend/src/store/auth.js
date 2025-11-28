
import { ref } from "vue";

export const isAuthenticated = ref(!!localStorage.getItem("access"));

export const loginUser = (access, refresh) => {
  localStorage.setItem("access", access);
  localStorage.setItem("refresh", refresh);
  isAuthenticated.value = true;
};

export const logoutUser = () => {
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
  isAuthenticated.value = false; 
};