import axios from "./axios";

export const getcategoRequest = () => axios.get("/catego");
export const createcategoRequest = (cate) => axios.post("/catego", cate);
export const updatecategoRequest = (id, cate) => axios.put(`/catego/${id}`, cate);
export const deletecategoRequest = async (id) => axios.delete(`/catego/${id}`);
export const getcateRequest = async (id) => axios.get(`/catego/${id}`);