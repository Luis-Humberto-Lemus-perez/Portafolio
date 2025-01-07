import { useState } from "react";
import { BsSearchHeart } from "react-icons/bs";
import { RxCrossCircled } from "react-icons/rx";
import { MdDensityMedium } from "react-icons/md";
import { useAuth } from "@/context/AuthContext";
import { Link } from "react-router-dom";
import css from "./NavBar.module.scss";

function Navbarhook() {
  const { isAuthenticated, signout } = useAuth();
  //search bar toggle with search and cross button
  const [search, setSearch] = useState(false);
  const openSearchBar = () => {
    setSearch(true);
    console.log(search);
  };

  const closeSearchBar = () => {
    setSearch(false);
    console.log(search);
  };

  //toggle btn
  const [toggle, setToggle] = useState(false);
  const toggled = () => {
    setToggle((prev) => !prev);
    console.log(toggle);
  };
  return (
    <>
    <div className="mb-24">
    <div className={css.wrapper}>
        <div className={css.nav_left}>
          <h3>Task Manager</h3>
        </div>

        <div
          className={`${css.main_menu} ${toggle ? css["main_menu--open"] : {}}`}
        >
          <ul>
            <li>
            <Link to="/" className="btn btn-primary btn-sm">
            Home
          </Link>

            </li>
          
            {isAuthenticated ? (
              <>
              <li>
              <Link to="/tasks" className="btn btn-primary btn-sm">
                Dashboard
              </Link>
              </li>
                <li>
                <Link to="/task/new" className="btn btn-primary btn-sm">
                Add Task
              </Link>
                </li>
              
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
              <li>
              <Link to="/login" className="btn btn-primary btn-sm">
                Login
              </Link>
              </li>
               <li>
               <Link to="/register" className="btn btn-primary btn-sm">
                Register
              </Link>
               </li>
              
                
              </>
            )}

            
          </ul>
        </div>

        <div>
          <div className={css.btns}>
            <span>
              <RxCrossCircled
                className={search ? css.show_btn : css.hide_btn}
                onClick={closeSearchBar}
              ></RxCrossCircled>
            </span>
            <MdDensityMedium
              className={css.toggle_btn}
              onClick={toggled}
            ></MdDensityMedium>
          </div>
        </div>
      </div>

    </div>
      
    </>
  );
}

export default Navbarhook;
