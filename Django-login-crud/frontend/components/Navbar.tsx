"use client";

import { signOut, useSession } from "next-auth/react";
import Link from "next/link";

export default function Navbar()  {
  const { data: session } = useSession();

  return (
    
    <nav className="flex justify-between items-center  bg-slate-900 text-white  px-24 py-3">
      <h1 className="text-xl font-bold">NextAuth</h1>
      <div className="flex gap-x-2">
        <Link
          href="/"
          className="btn btn-primary btn-sm"
        >
          Home
        </Link>
        {session?.user ? (
          <>
            <Link
              href="/dashboard"
              className="btn btn-primary btn-sm"
            >
              Dashboard
            </Link>
            <button
              onClick={() => signOut()}
              className="btn btn-danger btn-sm"
            >
              Signout
            </button>
          </>
        ) : (
          <>
            <Link
              href="/login"
              className="btn btn-primary btn-sm"
            >
              Login
            </Link>
            <Link
              href="/register"
              className="btn btn-primary btn-sm"
            >
              Register
            </Link>
          </>
        )}
      </div>
    </nav>
   

    
  );

 
};
