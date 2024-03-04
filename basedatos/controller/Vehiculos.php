<?php
class VehiculosController{
    public function __construct(){
        require_once('models/VehiculosModel.php');
    }
    public function index(){
        require_once('models/VehiculosModel.php');
        $vehiculos = new Vehiculos_model();
        $data["titulo"] = "Vehiculos";
        $data["vehiculos"] = $vehiculos->get_vehiculos();
        require_once('view/vehiculos/vehiculos.php');
    }
    public function crear(){
        $data["titulo"] = "Vehiculos";
        require_once('view/vehiculos/create.php');
    }
    public function guardar(){
        //require_once('models/VehiculosModel.php');
        $vehiculos = new Vehiculos_model();
        $placa = $_POST['txtplaca'];
        $marca = $_POST['txtmarca'];
        $modelo = $_POST['txtmodelo'];
        $anio = $_POST['txtanio'];
        $color = $_POST['txtcolor'];
        $vehiculos->insertar($placa, $marca, $modelo, $anio, $color);
        $this->index();
    }
    public function editar($id){
        $data["id"] = $id;
        $vehiculos = new Vehiculos_model();
        $data["vehiculos"] = $vehiculos->get_vehiculo($id);
        require_once('view/vehiculos/editar.php');
    }
    public function eliminar($id){
        $vehiculos = new Vehiculos_model();
    
        $vehiculos->eliminar($id);
        $this->index();
    }
    public function actualizar(){
        $vehiculos = new Vehiculos_model();
        $id = $_POST['id'];
        $placa = $_POST['txtplaca'];
        $marca = $_POST['txtmarca'];
        $modelo = $_POST['txtmodelo'];
        $anio = $_POST['txtanio'];
        $color = $_POST['txtcolor'];
        $vehiculos->editar($id, $placa, $marca, $modelo, $anio, $color);
        $this->index();
    }
}

?>