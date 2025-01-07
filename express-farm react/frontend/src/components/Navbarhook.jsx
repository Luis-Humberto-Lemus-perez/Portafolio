import { useState } from "react";
import { RxCrossCircled } from "react-icons/rx";
import { MdDensityMedium } from "react-icons/md";
import { useAuth } from "@/context/AuthContext";
import { Link } from "react-router-dom";
import css from "./Navbar.module.scss";

function Navbarhook() {
  const { isAuthenticated, signout, role } = useAuth();
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
  const reload = async  () => {
    signout();
    
         

  }
  return (
    <>
      <div className="container flex flex-wrap mx-auto">
        <div className={css.wrapper}>
          <div className={css.nav_left}>
            <h3 className="text-white">Task Manager</h3>
          </div>

          <div
            className={`${css.main_menu} ${
              toggle ? css["main_menu--open"] : {}
            }`}
          >
            <ul>
              <li>
                <Link to="/" className="btn btn-primary btn-sm text-white">
                  Home
                </Link>
              </li>
              <li>
                <Link to="/farmacia" className="btn btn-primary btn-sm text-white">
                  Farmacia
                </Link>
              </li>
              <li>
                <Link to="/about" className="btn btn-primary btn-sm text-white">
                  about
                </Link>
              </li>
              <li>
                <Link to="/contact" className="btn btn-primary btn-sm text-white">
                  contact
                </Link>
              </li>
              {isAuthenticated  && role == 'admin'? (
                <>
                  <li>
                    <Link to="/dashboard" className="btn btn-primary btn-sm text-white">
                      Dashboard
                    </Link>
                  </li>
                  <li>
                    <Link to="/medicine/new" className="btn btn-primary btn-sm text-white">
                      Add Medicine
                    </Link>
                  </li>

                  <button onClick={reload}className="text-white">Signout</button>
                </>
              
            
            ) : (
              
                
                <>
                  <li>
                    <Link to="/login" className="btn btn-primary btn-sm text-white">
                      Login
                    </Link>
                  </li>
                  <li>
                    <Link to="/register" className="btn btn-primary btn-sm text-white">
                      Register
                    </Link>
                  </li>
                </>
              )}
               <>
      {role === 'user' ? (
        <>
          <button onClick={signout} className="text-white">Signout</button>
        </>
      ) : (
        <>
         
        </>
      )}
    </>
             
            </ul>
          </div>

          <div className="text-white">
            <div className={css.btns}>
              <span >
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
