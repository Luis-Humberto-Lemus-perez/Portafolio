<?php
	
	require_once "confi/config.php";
	require_once "core/routes.php";
	require_once "confi/db.php";
	require_once "controller/Vehiculos.php";
	
	if(isset($_GET['controller'])){
		
		$controlador = cargarControlador($_GET['controller']);
		
		if(isset($_GET['action'])){
			if(isset($_GET['id'])){
				cargarAccion($controlador, $_GET['action'], $_GET['id']);
				} else {
				cargarAccion($controlador, $_GET['action']);
			}
			} else {
			cargarAccion($controlador, ACCION_PRINCIPAL);
		}
		
		} else {
		
		$controlador = cargarControlador(CONTROLADOR_PRINCIPAL);
		$accionTmp = ACCION_PRINCIPAL;
		$controlador->$accionTmp();
	}
?>