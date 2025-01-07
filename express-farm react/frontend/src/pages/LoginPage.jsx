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
import {Message} from "../components/ui/Message";
import { useAuth } from "../context/AuthContext";
import { Link , useNavigate} from 'react-router-dom'


function LoginPage() {
    const navigate = useNavigate();
    const {
      register,
      handleSubmit,
      formState: { errors },
    } = useForm();
    const {isAuthenticated,signin, errors:signinErrors,role}=useAuth();
    useEffect(() => {
      if (isAuthenticated && role=="admin") navigate("/dashboard");
        if (isAuthenticated && role=="user") navigate("/farmacia");
    }, [isAuthenticated,role]);
    const onSubmit = handleSubmit(async (values) => {
      signin(values);
    });



  return (
    <div className="h-screen flex justify-center items-center">
    <Card className="bg-zinc-800 text-white">
      <CardHeader>
        <CardTitle>Login</CardTitle>
      </CardHeader>
      {
      signinErrors.map((error,i) => (
        <Message message={error} key={i} />
      ))

    }
      <CardContent>
        <form onSubmit={onSubmit}>
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
            Login
          </Button>
        </form>
      </CardContent>
      <CardFooter>
        <p>
          Don't have an account?{" "}
          <Link to="/register" className="text-blue-500">
            Register
          </Link>
        </p>
      </CardFooter>
    </Card>
  </div>
  )
}

export default LoginPage