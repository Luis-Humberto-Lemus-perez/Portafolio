
<?php
/*
$contraseña = "";
$usuario = "root";
$nombre_bd= "crudphp";
try {
    $bd = new PDO(
        'mysql:host=localhost;
        dbname=' . $nombre_bd,
        $usuario, 
        $contraseña,
        array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8")
    );
    //echo "conectado";
} catch (Exception $e) {
    echo "Error de conexion".$e->getMessage();
}*/


class Conexion{
 
    public function  conexion()

    {
        $contraseña = "";
        $usuario = "root";
        $nombre_bd= "crudphp";
        try{
             $con = new mysqli("localhost",$usuario,$contraseña,$nombre_bd);
            //echo "conectado";
            return $con;
        }catch(Exception $e){
            echo "Error de conexion".$e->getMessage();
        }
       
        
    }

    public function getConexion($con){
        $query= $con->query("SELECT * FROM usuario;");
        $retorno = [];
        $i = 0;
        while ($fila = $query->fetch_assoc()) {
            $retorno[$i] = $fila;
            $i++;
        }
        return $retorno;
    }
    public function insertUsuarios($con,$nombre,$edad,$signo){
        $query= $con->query("INSERT INTO usuario(nombre,edad,signo) VALUES ('$nombre','$edad','$signo');");
        if ($query) {
            return true;
        }else{
            return false;
        }
    }

}
?>