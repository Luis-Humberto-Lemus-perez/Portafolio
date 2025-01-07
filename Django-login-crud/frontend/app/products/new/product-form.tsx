'use client';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import React from "react";
import { useForm } from "react-hook-form";
import {createProduct, getProduct, updateProduct} from '../../api/task.api'
import { useSession } from "next-auth/react";
import { useRouter, useParams } from "next/navigation";

export  function ProductForm({product}:any) {
    const { data: session, status } = useSession();
    
   
  const { register, handleSubmit } = useForm({
    defaultValues: {
        title: product?.title,
        description: product?.description,
        done: product?.done
       
    }
  });
  const router = useRouter();
  const params = useParams<{id: string}>();
 
  const onSubmit = handleSubmit(async (data) => {
   
    if(!params?.id){
        console.log("creando")
    
    await createProduct(session,{
        ...data
         

        
    })
   
    }
    console.log(data)
    
    router.push('/dashboard')
    router.refresh()

  });
  return (
    <form onSubmit={onSubmit}>
      <Label>Product Name</Label>
      <Input {...register("title")} />
      <Label>Description</Label>
      <Input {...register("description")} />
      <Label>Done</Label>
      <Input {...register("done")} />
      <Button>
     
          Create task
    
      </Button>
    </form>
  );
}

export default ProductForm;