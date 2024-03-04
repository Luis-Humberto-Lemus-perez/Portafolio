<?php 
require("models/conexion.php");
$db= new Conexion();
$con=$db->conexion();
$usuarios=$db->getConexion($con);
require("views/V_usuarios.php");


?>