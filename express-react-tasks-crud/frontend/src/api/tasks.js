import axios from "./axios";

export const getTasksRequest = () => axios.get("/tasks");
export const createTasksRequest = (task) => axios.post("/tasks", task);
export const updateTasksRequest = (id, task) => axios.put(`/tasks/${id}`, task);
export const deleteTasksRequest = async (id) => axios.delete(`/tasks/${id}`);
export const getTaskRequest = async (id) => axios.get(`/tasks/${id}`);
