from .entities.Product import Product


class ModelProduct:
    @classmethod
    def listar(self, db):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, codigo, nombre, cantidad, precio FROM productos ORDER BY nombre ASC"

            cursor.execute(sql)
            datos = cursor.fetchall()

            productos = []
            for fila in datos:

                pro = Product(fila[0], fila[1], fila[2], fila[3], fila[4])

                productos.append(pro)

            return productos

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def crear(self, db, codigo, nombre, cantidad, precio):
        try:
            print(codigo, nombre, cantidad, precio)
            cursor = db.connection.cursor()

            cursor.execute(
                "INSERT INTO productos (codigo, nombre, cantidad, precio) VALUES(%s,%s,%s,%s)",
                (codigo, nombre, cantidad, precio))
            db.connection.commit()

            return "Producto creado exitosamente"

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete(self, db, id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("DELETE FROM productos WHERE id = {0}".format(id))
            db.connection.commit()
            return "Producto eliminado exitosamente"
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_by_id(self, db, id):
        try:
            
            cursor = db.connection.cursor()
           
            cursor.execute('SELECT * FROM productos WHERE id ={}'.format(id))
            row = cursor.fetchall()
            cursor.close()
          
            for fila in row:
                pro = Product(fila[0], fila[1], fila[2], fila[3], fila[4])
                
            if pro != None:
                
                return pro
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def update(self, db, id, codigo, nombre, cantidad, precio):
        try:

           
            cursor = db.connection.cursor()
            
            cursor.execute(
            "UPDATE productos SET codigo = %s, nombre = %s, cantidad = %s, precio = %s WHERE id = %s",(codigo, nombre, cantidad, precio, id))
            db.connection.commit()
            return "Producto actualizado exitosamente"
        except Exception as ex:
            raise Exception(ex)