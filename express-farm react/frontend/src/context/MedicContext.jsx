import { createContext, useState, useContext } from "react";
import {
  createmedicineRequest,
  getmedicineRequest,
 deletemedicineRequest,getmedicRequest,
 updatemedicineRequest, storemedicinerequest
} from "../api/medicine";
import { get } from "react-hook-form";

const MedicContext = createContext();
export const useMedic = () => {
  const context = useContext(MedicContext);
  if (!context) {
    throw new Error("useTask must be used within TaskProvider");
  }
  return context;
};
export function MedicProvider({ children }) {
  const [medics, setMedic] = useState([]);
  
  const getMedic = async () => {
    try {
      const res = await getmedicineRequest();
      setMedic(res.data);
    } catch (error) {
      console.log(error);
    }
  };
  const createMedic = async (medic) => {
    try {
        console.log(medic);
        const res = await createmedicineRequest(medic);
        console.log(res.data)
        
    } catch (error) {
        console.log(error);
    }
   

   
  };
  const deleteMedic = async (id) => {
    try {
      const res = await deletemedicineRequest(id);
      if (res.status === 204) setMedic(medics.filter((medic) => medic._id !== id));
      
    } catch (error) {
      console.log(error);
    }
  };
  const getMedicById = async (id) => {
    try {
        const res = await getmedicRequest(id);
        return res.data;
    } catch (error) {
        console.log(error);
    }
  }
  const updateMedic = async (id, medic) => {
    try {
        await updatemedicineRequest(id, medic);
    } catch (error) {
        
    }
  }
  const storeMedic = async (id, stock) => {
    try {
        await storemedicinerequest(id, stock);
    } catch (error) {
        console.log(error);
    }
  }
  return (
    <MedicContext.Provider
      value={{
        medics,
        createMedic,
        getMedic,
        deleteMedic,
        getMedicById,
        updateMedic,
        storeMedic,
      }}
    >
      {children}
    </MedicContext.Provider>
  );
}
