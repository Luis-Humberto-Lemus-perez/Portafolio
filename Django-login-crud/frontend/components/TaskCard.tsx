"use client";
import { useRouter } from "next/navigation";
import { Button } from "./ui/button";
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "./ui/card";
import  {deleteProduct} from "@/app/api/task.api"
import { useSession } from "next-auth/react";

export function ProductCard({product}:any) {
    const { data: session, status } = useSession();
    const router = useRouter()
  
    async function handleDelete(id: any) {
       await deleteProduct(session,id)
       router.refresh()
    }

    
  return (
    <Card
    onClick={() => {
      router.push(`/products/${product.id}`);
    }} >
           
    <CardHeader 
    
    >
    <CardTitle className="flex justify-between">
      {product.title}
     
    </CardTitle>

    </CardHeader>
    

    <CardContent>
      <p>{product.description}</p>
      
    </CardContent>
    <CardFooter className="flex justify-between">
    <Button className="mt-5"
    onClick={(e) => {
        e.stopPropagation();
        router.push(`/products/${product.id}/edit`);
      }}
    >Edit Product</Button>
    <Button className="mt-5" variant="destructive"
    onClick={(e)=> {
    e.stopPropagation()
    handleDelete(product.id)}}>Eliminar</Button>
    </CardFooter>
  </Card>
  )
}
