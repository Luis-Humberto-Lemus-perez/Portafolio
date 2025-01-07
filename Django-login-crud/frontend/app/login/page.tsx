"use client";

import Navbar  from "@/components/Navbar";
import { signIn } from "next-auth/react";
import { useRouter } from "next/navigation";
import { useState } from "react";


const LoginPage = () => {
  const [errors, setErrors] = useState<string[]>([]);
  const [username, setusername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const router = useRouter();

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setErrors([]);

    const responseNextAuth = await signIn("credentials", {
      username,
      password,
      redirect: false,
    });

    if (responseNextAuth?.error) {
      setErrors(responseNextAuth.error.split(","));

      return;
    }

    router.push("/dashboard");
  };

  return (
    
    <div className=" ">
      <Navbar/>
      <div className="row">
        <div className="h-[calc(100vh-7rem)] flex justify-center items-center">
          <form onSubmit={handleSubmit} className="w-1/4">
            <h1 className="text-slate-200 font-bold text-4xl mb-4">Login</h1>

            <label
              htmlFor="email"
              className="text-slate-500 mb-2 block text-sm"
            >
              Username:
            </label>
            <input
              type="text"
              className="p-3 rounded block mb-2 bg-slate-900 text-slate-300 w-full"
              placeholder="user@email.com"
              name="username"
              value={username}
              onChange={(event) => setusername(event.target.value)}
            />

            <label
              htmlFor="password"
              className="text-slate-500 mb-2 block text-sm"
            >
              Password:
            </label>
            <input
              type="password"
              className="p-3 rounded block mb-2 bg-slate-900 text-slate-300 w-full"
              placeholder="******"
              name="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
            />

            <button className="w-full bg-blue-500 text-white p-3 rounded-lg mt-2">
              Login
            </button>
            {errors.length > 0 && (
          <div
            className="p-2 mt-2 text-sm text-red-800 rounded-lg bg-red-50 dark:text-red-400
           flex justify-center items-center"
            role="alert"
          >
            <ul className="">
              {errors.map((error) => (
                <li className="font-medium" key={error}>
                  {error}
                </li>
              ))}
            </ul>
          </div>
        )}
          </form>
        </div>

       
      </div>
    </div>
  );
};
export default LoginPage;
