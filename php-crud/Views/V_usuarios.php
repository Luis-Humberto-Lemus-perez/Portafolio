<?php include 'Views/header.php'?>
<?php
    /*
    include_once 'models/conexion.php';
    $sentencia = $bd->query("SELECT * FROM usuario;");
    $usuarios = $sentencia->fetchAll(PDO::FETCH_OBJ);
    //print_r($usuarios);*/
?>

<div class="contaider mt-5">
    <div class="row justify-content-center">
        <div class="col-md-7">
            <!--inicio mensage de alerta-->
            <?php
                if (isset($_GET['mensaje'])) {
                    if ($_GET['mensaje'] == 'falta') {
            ?>
            <div class="alert alert-danger alert-dismissible fade show" role="alert">
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            
                <strong>Error al registrar faltan datos</strong> You should check in on some of those fields below.
            </div>
            <?php

                    }}
            ?>
            <?php
                if (isset($_GET['mensaje'])) {
                    if ($_GET['mensaje'] == 'registrado') {
            ?>
            <div class="alert alert-success alert-dismissible fade show" role="alert">
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            
                <strong>registrado</strong>Datos agregados correctamente.
            </div>
            <?php

                    }}
            ?>
            
            <!--fin mensage de alerta-->
            <div class="card">
                <div class="card-header">
                    Lista de Usuarios
                </div>
                <div class="p-4">
                    <div class="table-responsive align-middle">
                        <table class="table table-primary">
                            <thead>
                                <tr>
                                    <th scope="col">#</th>
                                    <th scope="col">Nombre</th>
                                    <th scope="col">Edad</th>
                                    <th scope="col">signo</th>
                                    <th scope="col" colspan="2">Opciones</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php
                                    foreach ($usuarios as $dato) {


                                ?>
                                <tr class="">
                                    <td scope="row"><?php echo $dato['codigo']; ?></td>
                                    <td><?php echo $dato['nombre']; ?></td>
                                    <td><?php echo $dato['edad']; ?></td>
                                    <td><?php echo $dato['signo']; ?></td>
                                    <td>editar</td>
                                    <td>eliminar</td>
                                </tr>
                                <?php
                                    }
                                ?>
                            </tbody>
                        </table>
                    </div>
                    
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card">
                <div class="card-header">
                    Ingresar Usuarios
                    <form  class="p-4" method="POST" action="C_registrar.php">
                        <div class="mb-3">
                            <label class="from-label">Nombre: </label>
                            <input type="text" class="form-control" name="txtnombre" autofocus required>

                        </div>
                        <div class="mb-3">
                            <label class="from-label">Edad: </label>
                            <input type="number" class="form-control" name="txtedad" autofocus required>

                        </div>
                        <div class="mb-3">
                            <label class="from-label">Signo: </label>
                            <input type="text" class="form-control" name="txtsigno" autofocus required>

                        </div>
                        <div class="d-grid">
                            <input type="hidden" name="oculto" value="1">
                            <input type="submit" class="btn btn-primary" value="Registrar">
                        </div>

                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
<?php include 'Views/footer.php'?>