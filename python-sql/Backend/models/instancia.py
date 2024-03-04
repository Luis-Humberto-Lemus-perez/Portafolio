from utils.db import db
class Instancias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idcliente= db.Column(db.String(80))
    iden= db.Column(db.String(80), unique=True)
    idconfi= db.Column(db.String(80))
    nombre=db.Column(db.String(80))
    fecha_inicio=db.Column(db.String(80))
    estado=db.Column(db.String(80))
    fecha_final=db.Column(db.String(80))

    def __init__(self, idcliente, iden, idconfi, nombre, fecha_inicio, estado, fecha_final):
        self.idcliente = idcliente
        self.iden = iden
        self.idconfi = idconfi
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.estado = estado
        self.fecha_final = fecha_final