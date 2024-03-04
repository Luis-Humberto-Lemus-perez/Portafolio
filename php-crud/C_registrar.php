<?php 
    include_once 'Controllers/C_verusuarios.php';

    #print_r($_POST);*/

    if ( empty($_POST['oculto']) || empty($_POST['txtnombre']) || empty($_POST['txtedad']) || empty($_POST['txtsigno'])){
        echo "No se puede registrar faltan datos";
        header("location:index.php?mensage=falta");
        exit();
    }
    
    $nombre = $_POST['txtnombre'];
    //print_r($nombre);
    $edad = $_POST['txtedad'];
    $signo = $_POST['txtsigno'];
   // require('Views/V_usuarios.php');
    //include "C_registrar.php";

    $nombre = $_POST['txtnombre'];
    #print_r($nombre);
    $edad = $_POST['txtedad'];
    $signo = $_POST['txtsigno'];
    //$sql_agregar = $bd->prepare("INSERT INTO usuario(nombre,edad,signo) VALUES (?,?,?)");
    //$reultado = $sql_agregar->execute([$nombre,$edad,$signo]);
    $resultado = $db->insertUsuarios($con,$nombre,$edad,$signo);
    if ($resultado === TRUE) {
        echo "Insertado correctamente";
        header("location:index.php?mensaje=registrado");
    } else {
        header("location:index.php?mensaje=noregistrado");
        exit();
    }
    /*
    //$sql_agregar = $bd->prepare("INSERT INTO usuario(nombre,edad,signo) VALUES (?,?,?)");
    //$reultado = $sql_agregar->execute([$nombre,$edad,$signo]);
    $resultado = $con->insertUsuarios($nombre,$edad,$signo);
    if ($reultado === TRUE) {
        echo "Insertado correctamente";
        header("location:index.php?mensaje=registrado");
    } else {
        header("location:index.php?mensaje=noregistrado");
        exit();
    }
    #require("views/V_usuarios.php");  */
    
?>