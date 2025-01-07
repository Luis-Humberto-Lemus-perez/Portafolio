
'use client';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import * as React from 'react'
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {ProductForm} from './editform'
import { getProduct, updateProduct } from '../../../api/task.api'
import Link from 'next/link'
import { Button, buttonVariants } from '@/components/ui/button'
import { useSession } from 'next-auth/react';
import { useState } from 'react';

import { useParams, useRouter } from 'next/navigation'
import { useForm } from 'react-hook-form';



function ProductsEditPage ({params}) {

    const { data: session, status } = useSession();
    const [products, setProducts] = useState([]);

    const { id } = params
    console.log(id)
   
    const getuser = async () => {
        const pro = await getProduct(session, id);
        setProducts(pro)
    }
    
    const {handleSubmit } = useForm({
   
       
      });
      
      
      const router = useRouter();
  
    
      const onSubmit = handleSubmit(async (data) => {
        const res = await updateProduct(session, id, {
          ...data,
        });
        console.log(res)
    
        router.push("/dashboard");
        router.refresh();
      });
  return (
     <div>
      <Button onClick={getuser}>Get</Button>
      <div>
        {products.map((product: any) => (
            <div key={product.id}>
                <h1>{product.title}</h1>
                <p>{product.description}</p>
                <p>{product.done}</p>
            </div>
          ))}
      </div>
      <div className="h-screen flex justify-center items-center">
      <Card >
        <CardHeader>
          <CardTitle>
            Create Product
            <Link className={buttonVariants()} href="/dashboard">
              Go back
            </Link>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={onSubmit}>
            <Label>Title</Label>
            <Input  />
            <Label>Description</Label>
            <Input  />
            <Label>done</Label>
            <Input  />
            <Button> Update Product</Button>
          </form>
        </CardContent>
      </Card>
    </div>
      </div>
    
  )
}

export default ProductsEditPage