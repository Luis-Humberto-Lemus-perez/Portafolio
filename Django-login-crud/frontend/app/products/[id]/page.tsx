import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { getProduct } from "../../api/task.api";
import Link from "next/link";
import {buttonVariants} from '@/components/ui/button'
import { useSession } from "next-auth/react";
import Getid, { Getidi } from "./getid";


async function ProducDetailpage({params}:any) {
  
    const { id } = await params
    
    

  return(
    <Getidi id={id}/>

  ) 
    
}
export default ProducDetailpage