import { z } from "zod";
export const createmedicSchema = z.object({
  name: z.string({
    required_error: "Name is required",
  }),
  description: z
    .string({
      required_error: "Description is required",
    }),
    img: z.string({
      required_error: "Img is required",
    }),
    precio: z.number({
      required_error: "Precio is required",
    }),
    stock: z.number({
      required_error: "Stock is required",
    }),
    category: z.string({
      required_error: "Category is required",
    }),
});