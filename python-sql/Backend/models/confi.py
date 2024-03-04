from utils.db import db

class Confi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idencarte= db.Column(db.String(80)  )
    iden= db.Column(db.String(80), unique=True)
    nombre=db.Column(db.String(80))
    descripcion=db.Column(db.String(80))


    def __init__(self, idencarte, iden, nombre, descripcion):
        self.idencarte = idencarte
        self.iden = iden
        self.nombre = nombre
        self.descripcion = descripcion