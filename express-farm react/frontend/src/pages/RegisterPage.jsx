import React, {useEffect} from "react";
import { useForm } from "react-hook-form";
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
  CardFooter,
} from "../components/ui/card";
import { Label } from "../components/ui/label";
import { Input } from "../components/ui/input";
import { Button } from "../components/ui/button";
import { useNavigate, Link } from "react-router-dom";
import {Message} from "../components/ui/Message";
import { useAuth } from "../context/AuthContext";
function RegisterPage() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();
  const { signup, isAuthenticated, errors: registerErrors } = useAuth();
  const navigate = useNavigate();
  useEffect(() => {
    if (isAuthenticated) navigate("/login");
  }, [isAuthenticated]);
  const onSubmit = handleSubmit(async (values) => {
    signup(values);
  });
  return (
    <div className="h-screen flex justify-center items-center">
      <Card className="bg-zinc-800 text-white">
        <CardHeader>
          <CardTitle>Register</CardTitle>
        </CardHeader>
        <CardContent>
        {
        registerErrors.map((error,i) => (
          <Message message={error} key={i} />
        ))

      }
          <form onSubmit={onSubmit}>
            <Label>Username</Label>
            <Input
              type="text"
              {...register("username", { required: true })}
              className="bg-zinc-700 text-white mb-2"
            />
            {errors.username && (
              <p className="text-red-500 mb-2">This field is required</p>
            )}
            <Label>Email</Label>
            <Input
              type="email"
              {...register("email", { required: true })}
              className="bg-zinc-700"
            />
            {errors.email && (
              <p className="text-red-500">This field is required</p>
            )}
            <Label>Password</Label>
            <Input
              type="password"
              {...register("password", { required: true })}
              className="bg-zinc-700 text-white mb-2"
            />
            {errors.password && (
              <p className="text-red-500">This field is required</p>
            )}
            <Button type="submit" className="my-2 bg-zinc-700">
              Register
            </Button>
          </form>
        </CardContent>
        <CardFooter>
          <p>
            Already have an account?{" "}
            <Link to="/login" className="text-blue-500">
              Login
            </Link>
          </p>
        </CardFooter>
      </Card>
    </div>
  );
}

export default RegisterPage;
