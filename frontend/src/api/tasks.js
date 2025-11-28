import axios from "axios";

const API = "http://127.0.0.1:8000/api/tasks/";

export const getTasks = () =>
  axios.get(API, {
    headers: { Authorization: `Bearer ${localStorage.getItem("access")}` }
  });

export const createTask = (task) =>
  axios.post(API, task, {
    headers: { Authorization: `Bearer ${localStorage.getItem("access")}` }
  });

export const updateTask = (id, task) =>
  axios.put(API + id + "/", task, {
    headers: { Authorization: `Bearer ${localStorage.getItem("access")}` }
  });

export const deleteTask = (id) =>
  axios.delete(API + id + "/", {
    headers: { Authorization: `Bearer ${localStorage.getItem("access")}` }
  });
