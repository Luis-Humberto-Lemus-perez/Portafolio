<?php
    $AbsRoute = 'C:/xampp/htdocs/basedatos/';
    require_once ($AbsRoute."view/templates/header.php");
?>


        <div class="col-md-4">
            <div class="card">
                <div class="card-header">
                    Editar vehiculo
                    <form  class="p-4" method="POST" action="index.php?controller=vehiculos&action=actualizar">
                        <input type="hidden" name="id" value="<?php echo $data['id'] ?>">
                        <div class="mb-3">
                            <label class="from-label">placa: </label>
                            <input type="text" class="form-control" name="txtplaca" autofocus required value="<?php echo $data['vehiculos']['placa']?> ">

                        </div>
                        <div class="mb-3">
                            <label class="from-label">marca: </label>
                            <input type="text" class="form-control" name="txtmarca" autofocus required value="<?php echo $data['vehiculos']['marca']?> ">

                        </div>
                        <div class="mb-3">
                            <label class="from-label">modelo: </label>
                            <input type="text" class="form-control" name="txtmodelo" autofocus required value="<?php echo $data['vehiculos']['modelo']?> ">

                        </div>
                        <div class="mb-3">
                            <label class="from-label">año: </label>
                            <input type="int" class="form-control" name="txtanio" autofocus required value="<?php echo $data['vehiculos']['anio']?> ">

                        </div>
                        <div class="mb-3">
                            <label class="from-label">color: </label>
                            <input type="text" class="form-control" name="txtcolor" autofocus required value="<?php echo $data['vehiculos']['color']?> ">

                        </div>
                        <div class="d-grid">
                            <input type="submit" name="btnguardar" class="btn btn-primary" value="Editar">
                        </div>
                       

                    </form>
                </div>
            </div>
        </div>

<?php
    require_once ($AbsRoute."view/templates/fotter.php");
?>