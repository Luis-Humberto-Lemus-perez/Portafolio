import { useMedic } from "@/context/MedicContext";
import React, { useEffect } from "react";
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

function DashboardPage() {
  const { getMedic, medics } = useMedic();

  useEffect(() => {
    getMedic();
  }, []);

  return (
    <div className="grid sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-3">
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
          <img src={task.img} alt="" width={150}/>
            <p className="">{task.description}</p>
          </CardContent>
          <p className="flex justify-center">{task.stock}</p>
          <p className="flex justify-center">{task.category}</p>
          <CardFooter className="flex justify-between">
            <Button className="mt-5">Edit Product</Button>
            <Button className="mt-5" variant="destructive">
              Eliminar
            </Button>
          </CardFooter>
        </Card>
      ))}
    </div>
  );
}

export default DashboardPage;
