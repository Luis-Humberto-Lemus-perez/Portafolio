"use client";
import { useRouter } from "next/navigation";
import { Button } from "./ui/button";
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "./ui/card";
import  {deleteProduct} from "@/app/products/products.api"

export function ProductCard({product}:any) {
    const router = useRouter()
    async function handleDelete(id: any) {
       await deleteProduct(id)
       router.refresh()
    }

    
  return (
    <Card>
           
    <CardHeader 
    
    >
    <CardTitle className="flex justify-between">
      {product.name}
      <span className="text-sm font-bold text-gray-500">
        ${product.price}
      </span>
    </CardTitle>

    </CardHeader>
    <img src={product.image} alt=""
    onClick={() => {
        router.push(`/products/${product.id}`);
      }} 
    />

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
