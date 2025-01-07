'use client';
import { getProduct } from "@/app/api/task.api";
import { Button, buttonVariants } from "@/components/ui/button";
import { Card } from "@/components/ui/card"
import {CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useSession } from "next-auth/react";
import Link from "next/link";
import { useState } from "react";


export function Getidi({id}) {
    const { data: session, status } = useSession();
    const [products, setProducts] = useState([]);


    const getproc = async () => {
        const pro = await getProduct(session,id)
        setProducts(pro)
    }
    
    
   
  return (
    <div
    className="flex justify-center items-center h-screen"
  >
    <Card  onClick={getproc}>
    <CardHeader>
            <CardTitle className="flex justify-between">
                
                Product Detail: {products.id}
                <br />
                
                <Link
                    className={buttonVariants()}
                    href="/dashboard"
                >
                    Go back
                </Link>
            </CardTitle>
        </CardHeader>
             <p className="ml-4 mb-4 text-xs">Click here</p>
        <CardContent>
            <h1>{products.title}</h1>
            <p>{products.description}</p>
           
        </CardContent>
        
    </Card>

  </div>
    
  )
}

export default Getidi