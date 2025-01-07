import { useMedic } from "@/context/MedicContext";
import React, { useEffect, useState } from "react";
import { ImFileEmpty } from "react-icons/im";
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
  CardFooter,
} from "../components/ui/card";
import { Label } from "../components/ui/label";
import { Button } from "@/components/ui/button";
import { useAuth } from "@/context/AuthContext";
import { useNavigate } from "react-router-dom";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

function FarmaciaPage() {
  const { getMedic, medics, storeMedic } = useMedic();
  const [practices, setPractices] = useState(0);
  const { isisAuthenticated, role } = useAuth();

  useEffect(() => {
    getMedic();
    
  }, []);
  const navigate = useNavigate();
  const shop = async (id) => {
    if (!isisAuthenticated && role !== "user")
      return alert("Debes iniciar sesion");

    if (practices === 0) {
      return alert("Debes seleccionar una cantidad");
    }
    const stock = {
      stock: parseInt(practices),
    };
    try {
      await storeMedic(id, stock);
      return alert("Compra exitosa");
      

    } catch (error) {
      console.log(error);
    }
  };

  const handleStringToInt = (value) => {
    setPractices(parseInt(value));
  };

  return (
    <div className="grid sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-3  mt-28">
      {medics.map((task) => (
        <Card className="bg-zinc-800 text-white " key={task.id}>
          <CardHeader>
            <CardTitle className="flex justify-between">
              {task.name}
              <span className="text-sm font-bold text-gray-500">
                ${task.precio}
              </span>
            </CardTitle>
          </CardHeader>

          <CardContent>
            <img src={task.img} alt="" width={150} />
            <p className="">{task.description}</p>
          </CardContent>
          <p className="flex justify-center">{task.stock}</p>
          <p className="flex justify-center">{task.category}</p>
          <CardFooter className="flex justify-between">
            <Select className="bg-slate-500 " onValueChange={handleStringToInt}>
              <SelectTrigger className="w-[180px] text-gray-700">
                <SelectValue placeholder="Select a fruit" />
              </SelectTrigger>
              <SelectContent className="mt-28">
                <SelectGroup>
                  <SelectLabel>Cantidad</SelectLabel>
                  <SelectItem value="1">1</SelectItem>
                  <SelectItem value="2">2</SelectItem>
                  <SelectItem value="3">3</SelectItem>
                  <SelectItem value="4">4</SelectItem>
                  <SelectItem value="5">5</SelectItem>
                  <SelectItem value="6">6</SelectItem>
                  <SelectItem value="7">7</SelectItem>
                  <SelectItem value="8">8</SelectItem>
                  <SelectItem value="9">9</SelectItem>
                  <SelectItem value="10">10</SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>

            <Button className="mt-5" onClick={() => shop(task._id)}>
              Comprar
            </Button>
          </CardFooter>
        </Card>
      ))}
    </div>
  );
}

export default FarmaciaPage;
