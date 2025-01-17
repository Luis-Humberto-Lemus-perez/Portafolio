import { z } from "zod";

export const registerSchema = z.object({
  username: z.string({
    required_error: "Username is required",
  }),
  email: z
    .string({
      required_error: "email is required",
    })
    .email({
      message: "Invalid email",
    }),
  password: z
    .string({
      required_error: "Password is required",
    })
    .min({
      message: "Password must be at least 6 characters",
    }),
});
export const loginSchema = z.object({
  email: z.string().email(),
  password: z.string().min(6),
});
