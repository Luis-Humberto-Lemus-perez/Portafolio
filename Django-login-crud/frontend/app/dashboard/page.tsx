"use client";
import Navbar from "@/components/Navbar";
import { get } from "http";
import { useSession } from "next-auth/react";
import { useState } from "react";
import { getProducts } from "../api/task.api";
import { ProductCard } from "@/components/TaskCard";
import Link from "next/link";
import { Button, buttonVariants } from "@/components/ui/button";

const Dashboard = () => {
  const { data: session, status } = useSession();
  const [users, setuser] = useState([]);

  const [products, setProducts] = useState([]);

  if (status === "loading") {
    return <p>Loading...</p>;
  }

  const getuser = async () => {
    const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/notes`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        authorization: `Bearer ${session?.user?.token}`,
      },
    });

    const data = await res.json();

    setuser(data);
    const products = await getProducts(session);
    setProducts(products);
   
  };

  

  return (
    <div>
      <Navbar />
      <h1>Dashboard</h1>
      <Button onClick={getuser} className="btn btn-primary">
        Get products
      </Button>
      {users.length >= 0 && (
        <div>
          <ul className="">
            {users.map((pk) => (
              <li className="font-medium" key={pk}>
                {pk.username}
                <br />
                {pk.email}
              </li>
            ))}
          </ul>
        </div>
      )}
     
      <>
        <div className="flex justify-between">
          <h1 className="text-4xl font-bold">NextNestApp</h1>
          <Link href="/products/new" className={buttonVariants()}>
            Products New
          </Link>
        </div>
        <div className="grid sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-3">
          {products.map((product: any) => (
            <ProductCard product={product} key={product.id} />
          ))}
        </div>
      </>
    </div>
  );
};
export default Dashboard;
