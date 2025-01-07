"use client";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import React from "react";
import { useForm } from "react-hook-form";
import {
  createProduct,
  getProduct,
  updateProduct,
} from "../../../products/products.api";
import { useRouter, useParams } from "next/navigation";

export function ProductForm({ product }: any) {
  const { register, handleSubmit } = useForm({
    defaultValues: {
      name: product?.name,
      description: product?.description,
      price: product?.price,
      image: product?.image,
    },
  });
  const router = useRouter();
  const params = useParams<{ id: string }>();

  const onSubmit = handleSubmit(async (data) => {
    const res = await updateProduct(params.id, {
      ...data,
      price: parseFloat(data.price),
    });
    console.log(res);

    router.push("/");
    router.refresh();
  });
  return (
    <form onSubmit={onSubmit}>
      <Label>Product Name</Label>
      <Input {...register("name")} />
      <Label>Description</Label>
      <Input {...register("description")} />
      <Label>Price</Label>
      <Input {...register("price")} />
      <Label>Image</Label>
      <Input {...register("image")} />
      <Button> Update Product</Button>
    </form>
  );
}

export default ProductForm;
