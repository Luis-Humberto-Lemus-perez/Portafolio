/**'use client';
import { useSession } from 'next-auth/react';
import ProductsEditPage from './page';



export function session(params) {
    const {id} = params
    console.log(id)
    const { data: session, status } = useSession();
    const areglo = {'id':id,
    'session':session}
    

    return (
       <ProductsEditPage session={areglo}/>
    )
  
}
export default session**/

