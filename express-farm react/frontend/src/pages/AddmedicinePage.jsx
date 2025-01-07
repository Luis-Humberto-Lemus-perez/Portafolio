import React, { useEffect } from "react";
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
  CardFooter,
} from "../components/ui/card";
import { Label } from "../components/ui/label";
import { Input } from "../components/ui/input";
import { Button, buttonVariants } from "../components/ui/button";
import { Message } from "../components/ui/Message";
import { Textarea } from "../components/ui/textarea";
import { useForm } from "react-hook-form";
import { useCatego } from "../context/CategoryContext";
import { useNavigate, useParams, Link } from "react-router-dom";
import { useMedic } from "@/context/MedicContext";
import { useAuth } from "@/context/AuthContext";
function AddmedicinePage() {
  const { categos, createCatego, getCategos, idcate } = useCatego();
  const navigate = useNavigate();
  const {medics, createMedic}=useMedic();
  const {role}=useAuth()

  const { register, handleSubmit, setValue } = useForm();
  const { register: registermedic, handleSubmit: hanclemedic } = useForm();

    console.log(role)
  const onSubmit = handleSubmit((values) => {
   
    const catego = {
     name: values.name,
    description: values.description,
    };
    createCatego(catego);

    //navigate("/dashboard");
    
  });
  const onmedic = hanclemedic((values) => {
    try {
        console.log(idcate);
        console.log(role)
        const medic = {
            name: values.name,
            description: values.description,
            img: values.img,
            precio: parseInt(values.precio),
            stock: parseInt(values.stock),
            category: idcate,
          }
       
        createMedic(medic);
        navigate("/dashboard");
        
    } catch (error) {
        console.log("error");
    }
    
  });

  return (
    <div className="h-screen flex justify-center items-center">
      <Card className="bg-zinc-800 text-white">
        <CardHeader>
          <CardTitle className="flex justify-between">
            Create Medicine
            <Link className={buttonVariants()} to="/dashboard">
              Go back
            </Link>
          </CardTitle>
        </CardHeader>

        <CardContent>
          <div className="flex justify-between">
            <div >
              <form onSubmit={onSubmit}>
                <div>
                  <Label>Category</Label>
                </div>

                <Label>name</Label>
                <Input
                  type="text"
                  {...register("name", { required: true })}
                  autoFocus
                  className="bg-zinc-700"
                />

                <Label>Description</Label>
                <Textarea
                  rows="3"
                  placeholder="Enter description"
                  {...register("description", { required: true })}
                  className="bg-zinc-700 text-white"
                ></Textarea>

                <Button type="submit" className="my-2 bg-zinc-700">
                  Create category
                </Button>
              </form>
            </div>
            <div className="ml-8">
              <form onSubmit={onmedic}>
                <div>
                  <Label> create medicine</Label>
                </div>

                <Label>name</Label>
                <Input
                  type="text"
                  {...registermedic("name", { required: true })}
                  autoFocus
                  className="bg-zinc-700"
                />

                <Label>Description</Label>
                <Textarea
                  rows="3"
                  placeholder="Enter description"
                  {...registermedic("description", { required: true })}
                  className="bg-zinc-700 text-white"
                ></Textarea>
                <Label>img</Label>
                <Input
                  type="text"
                  {...registermedic("img", { required: true })}
                  autoFocus
                  className="bg-zinc-700"
                />
                <Label>price</Label>
                <Input
                  type="number"
                  {...registermedic("precio", { required: true })}
                  autoFocus
                  className="bg-zinc-700"
                />
                <Label>stock</Label>
                <Input
                  type="number"
                  {...registermedic("stock", { required: true })}
                  autoFocus
                  className="bg-zinc-700"
                />

                <Button type="submit" className="my-2 bg-zinc-700">
                  Create Medicine
                </Button>
              </form>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

export default AddmedicinePage;
