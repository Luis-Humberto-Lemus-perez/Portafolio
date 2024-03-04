from utils.db import db

class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    iden= db.Column(db.String(80), unique=True) 
    nombre=db.Column(db.String(80))
    usuario=db.Column(db.String(80))
    clave=db.Column(db.String(80))
    direccion=db.Column(db.String(80))
    correo=db.Column(db.String(80))
    deuda=db.Column(db.Float)
   
    def __init__(self, iden, nombre, usuario, clave, direccion, correo, deuda):
        self.iden = iden
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.direccion = direccion
        self.correo = correo
        self.deuda = deuda