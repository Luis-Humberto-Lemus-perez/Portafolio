"use client";
import { Button, buttonVariants } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import {
  createProduct,
  getProduct,
  updateProduct,
} from "../../../api/task.api";
import { useRouter, useParams } from "next/navigation";
import { useSession } from "next-auth/react";
import Link from "next/link";
import { get } from "http";

export function ProductForm({ product }: any) {
 
  const { data: session, status } = useSession();
  //const [products, setProducts] = useState([]);
  //const getproc = async () => {
  

  
  
  return (
    
  );
}

export default ProductForm;
