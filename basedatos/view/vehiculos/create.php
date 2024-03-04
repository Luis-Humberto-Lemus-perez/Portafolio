<?php
    $AbsRoute = 'C:/xampp/htdocs/basedatos/';
    require_once ($AbsRoute."view/templates/header.php");
?>


        <div class="col-md-4">
            <div class="card">
                <div class="card-header">
                    Ingresar Usuarios
                    <form  class="p-4" method="POST" action="index.php?controller=vehiculos&action=guardar">
                        <div class="mb-3">
                            <label class="from-label">placa: </label>
                            <input type="text" class="form-control" name="txtplaca" autofocus required>

                        </div>
                        <div class="mb-3">
                            <label class="from-label">marca: </label>
                            <input type="text" class="form-control" name="txtmarca" autofocus required>

                        </div>
                        <div class="mb-3">
                            <label class="from-label">modelo: </label>
                            <input type="text" class="form-control" name="txtmodelo" autofocus required>

                        </div>
                        <div class="mb-3">
                            <label class="from-label">año: </label>
                            <input type="int" class="form-control" name="txtanio" autofocus required>

                        </div>
                        <div class="mb-3">
                            <label class="from-label">color: </label>
                            <input type="text" class="form-control" name="txtcolor" autofocus required>

                        </div>
                        <div class="d-grid">
                            <input type="submit" name="btnguardar" class="btn btn-primary" value="Guardar">
                        </div>
                       

                    </form>
                </div>
            </div>
        </div>

<?php
    require_once ($AbsRoute."view/templates/fotter.php");
?>