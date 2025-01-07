"use client";

import { signIn, signOut, useSession } from "next-auth/react";

export default function ButtonAuth() {
  const { data: session, status } = useSession();
  
  if (status === "loading") {
    return <p>Loading...</p>;
  }

  if (session) {
    return (
      <>
        Signed in as {session.user?.username}<br />
        <button
          onClick={() => signOut()}
          className="bg-red-700  text-white px-4 py-2 rounded-md"
        >
          Sign out
        </button>
      </>
    );
  }
  return (
    <>
      Not signed in <br />
      <button
        onClick={() => signIn()}
        className="bg-green-950  text-white px-4 py-2 rounded-md"
      >
        Sign in
      </button>
    </>
  );
}
