import { createContext, useState, useContext } from "react";
import {
  createcategoRequest,
  getcategoRequest,
 deletecategoRequest,getcateRequest, updatecategoRequest
} from "../api/category";
import { get } from "react-hook-form";

const CategoContext = createContext();
export const useCatego = () => {
  const context = useContext(CategoContext);
  if (!context) {
    throw new Error("useTask must be used within TaskProvider");
  }
  return context;
};
export function CategoProvider({ children }) {
  const [categos, setCatego] = useState([]);
  const [idcate, setIdcate] = useState("");
  const getCategos = async () => {
    try {
      const res = await getcategoRequest();
      setCatego(res.data);
    } catch (error) {
      console.log(error);
    }
  };
  const createCatego = async (catego) => {
    try {
    console.log("catego");
    const res = await createcategoRequest(catego);
    console.log(res.data)
    setIdcate(res.data.id);
        
    } catch (error) {
      console.log("error");
        
    }
    
    //console.log(res.data.id);
  };
  const deleteCatego = async (id) => {
    try {
      const res = await deletecategoRequest(id);
      if (res.status === 204) setCatego(categos.filter((catego) => catego._id !== id));
      
    } catch (error) {
      console.log(error);
    }
  };
  const getCatego = async (id) => {
    try {
        const res = await getcateRequest(id);
        return res.data;
    } catch (error) {
        console.log(error);
    }
  }
  const updateCatego = async (id, catego) => {
    try {
        await updatecategoRequest(id, catego);
    } catch (error) {
        
    }
  }
  return (
    <CategoContext.Provider
      value={{
        categos,
        createCatego,
        getCategos,
        deleteCatego,
        getCatego,
        updateCatego,
        idcate,
      }}
    >
      {children}
    </CategoContext.Provider>
  );
}
