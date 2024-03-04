from utils.db import db
class Categorias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    iden= db.Column(db.String(80), unique=True, nullable=False)
    nombre = db.Column(db.String(80))
    descripcion=db.Column(db.String(80))
    cargaTrabajo=db.Column(db.String(80))

    def __init__(self, iden, nombre, descripcion, cargaTrabajo):
        self.iden = iden
        self.nombre = nombre
        self.descripcion = descripcion
        self.cargaTrabajo=cargaTrabajo