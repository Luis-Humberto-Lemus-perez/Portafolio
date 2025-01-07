import { useAuth} from '@/context/AuthContext'
import React from 'react'
import { Navigate, Outlet } from 'react-router-dom'

function ProtectedRoute() {
    const {loading, isAuthenticated, role}=useAuth()

    if (loading) {
        return <div>Loading...</div>
    }
    if (!loading && !isAuthenticated ) {
        return <Navigate to="/login" replace/>
        
    }
    if (role==="user") {
        return <Navigate to="/" replace/>
    }
  return (
    <Outlet />
  )
}

export default ProtectedRoute