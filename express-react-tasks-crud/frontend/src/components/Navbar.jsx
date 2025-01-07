import { useRef } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "@/context/AuthContext";
import { FaBars, FaTimes } from "react-icons/fa";
function Navbar() {
  const { isAuthenticated, signout } = useAuth();

  const navRef = useRef();

  
  return (
    <header>
      <nav
        
        className="flex justify-between items-center  bg-slate-900 text-white  px-24 py-3"
      >
        <h1 className="text-xl font-bold">Task Manager</h1>
        <div className="flex gap-x-2">
          <Link to="/" className="btn btn-primary btn-sm">
            Home
          </Link>
          {isAuthenticated ? (
            <>
              <Link to="/tasks" className="btn btn-primary btn-sm">
                Dashboard
              </Link>
              <Link to="/task/new" className="btn btn-primary btn-sm">
                Add Task
              </Link>
              <button
                onClick={() => {
                  signout();
                }}
                className="btn btn-danger btn-sm"
              >
                Signout
              </button>
            </>
          ) : (
            <>
              <Link to="/login" className="btn btn-primary btn-sm">
                Login
              </Link>
              <Link to="/register" className="btn btn-primary btn-sm">
                Register
              </Link>
            </>
          )}
        </div>
       
      </nav>
     
    </header>
  );
}

export default Navbar;
