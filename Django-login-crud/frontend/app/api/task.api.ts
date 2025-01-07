import { useSession } from "next-auth/react";
export const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL;
export async function getProducts( session: any ) {
  
  const res = await fetch(`${BACKEND_URL}/tasks`, {
        cache: "no-store",
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      authorization: `Bearer ${session?.user?.token}`,
    },
  });
  //console.log(BACKEND_URL)
  return await res.json();
}
export async function getProduct(session:any,id: string) {
  const data = await fetch(`${BACKEND_URL}/tasks/${id}/`, {
    cache: "no-store",
    headers: {
      "Content-Type": "application/json",
      
    authorization: `Bearer ${session?.user?.token}`,
    }
  });
  if (data.status === 200) {
    return await data.json();
  }
  
  return await data.json();
}
export async function createProduct(session:any,productData: any) {
        console.log(productData)
  const res = await fetch("http://localhost:8000/api/tasks/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      //cache: 'no-store'
      authorization: `Bearer ${session?.user?.token}`,
    },
    body:  JSON.stringify(productData)
    
  });
  const data = await res.json();
  console.log(data);
}
export async function deleteProduct(session: any,id: string) {
  const res = await fetch(`${BACKEND_URL}/tasks/${id}/`, {
    method: "DELETE",
    headers: {
      
      //cache: 'no-store'
      authorization: `Bearer ${session?.user?.token}`,
    },


    
  });
  if (res.status === 204) {
    const respon = {
      status: "success",
      message: "Product deleted successfully",
    }
    
    return respon;
  }
  console.log(res)
  return await res.json();
}

export async function updateProduct(session:any,id: string, newProduct: any) {
  const res = await fetch(`${BACKEND_URL}/tasks/${id}/`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      authorization: `Bearer ${session?.user?.token}`,
    },
    body: JSON.stringify(newProduct),
    cache: "no-store",
  });
  return await res.json();
}
