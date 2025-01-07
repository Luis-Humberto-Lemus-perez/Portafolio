import { Button } from "./components/ui/button";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import RegisterPage from "./pages/RegisterPage";
import { AuthProvider } from "./context/AuthContext";
import LoginPage from "./pages/LoginPage";
import ProtectedRoute from "./pages/ProtectedRoute";
import DashboardPage from "./pages/DashboardPage";
import Navbarhook from "./components/Navbarhook";
import AddmedicinePage from "./pages/AddmedicinePage";
import { CategoProvider } from "./context/CategoryContext";
import { MedicProvider } from "./context/MedicContext";
import FarmaciaPage from "./pages/FarmaciaPage";
import Nabvar from "./components/Nabvar";
function App() {
  return (
    <AuthProvider>
      <CategoProvider>
        <MedicProvider>
        <BrowserRouter>
        <Navbarhook/>
        <Routes>
          <Route path="/" element={<Button>Home</Button>} />
          <Route path="/about" element={<Button>About</Button>} />
          <Route path="/contact" element={<Button>Contact</Button>} />
          <Route path="/farmacia" element={<FarmaciaPage/>} />

          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route element={<ProtectedRoute />}>
            <Route path="/dashboard" element={<DashboardPage />} />
            <Route path="/medicine/new" element={<AddmedicinePage/>} />
          </Route>
        </Routes>
      </BrowserRouter>

        </MedicProvider>
      

      </CategoProvider>
      
    </AuthProvider>
  );
}

export default App;
