<?php
 $AbsRoute = 'C:/xampp/htdocs/basedatos/';
 require_once ($AbsRoute."view/templates/header.php")
 ?>
<div class="container">
    <div class="row">
        <div class="col-12">
            <h2 class="text-center"><?php echo $data['titulo'] ?></h2>
        </div>
    </div>
    <div class="row">
        <div class="col-12">
            <a href="index.php?controller=vehiculos&action=crear" class="btn btn-success">Crear</a>
        </div>
    </div>
    <div class="row">
        <div class="col-12">
            <table class="table table-striped table-hover">
                <thead>
                    <tr>
                        <th>placa</th>
                        <th>Marca</th>
                        <th>Modelo</th>
                        <th>Año</th>
                        <th>color</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                            <?php
                                    foreach ($data['vehiculos'] as $dato) {


                                ?>
                                <tr class="">
                                    <td scope="row"><?php echo $dato['placa']; ?></td>
                                    <td><?php echo $dato['marca']; ?></td>
                                    <td><?php echo $dato['modelo']; ?></td>
                                    <td><?php echo $dato['anio']; ?></td>
                                    <td><?php echo $dato['color']; ?></td>
                                    <?php 
                                        $id=  $dato['id'];
                                        $urleditar = "index.php?controller=vehiculos&action=editar&id=".$id;
                                        $urleliminar = "index.php?controller=vehiculos&action=eliminar&id=".$id;
                                        ?>
                                    <td><a href=<?php echo $urleditar ?>>Editar</a></td>
                                    <td><a href=<?php echo $urleliminar ?>> Eliminar</a></td>
                                </tr>
                                <?php
                                    }
                                ?>
                </tbody>
            </table>
        </div>
    </div>
<?php
    require_once ($AbsRoute."view/templates/fotter.php")
?>