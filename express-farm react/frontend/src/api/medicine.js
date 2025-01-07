import axios from "./axios";

export const getmedicineRequest = () => axios.get("/medicine");
export const createmedicineRequest = (medic) => axios.post("/medicine", medic);
export const updatemedicineRequest = (id, medic) => axios.put(`/medicine/${id}`, medic);
export const deletemedicineRequest = async (id) => axios.delete(`/medicine/${id}`);
export const getmedicRequest = async (id) => axios.get(`/medicine/${id}`);
export const storemedicinerequest = async (id, stock) => axios.put(`/stock/${id}`, stock);