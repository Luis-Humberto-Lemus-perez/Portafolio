from utils.db import db
class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idpro=db.Column(db.String(100), unique=True, nullable=False)
    nombre=db.Column(db.String(100))
    abrebiatura= db.Column(db.String(100))
    metrica=db.Column(db.String(100))
    tipo= db.Column(db.String(100))
    valor_hora= db.Column(db.Float)

    def __init__(self, idpro, nombre, abrebiatura, metrica, tipo, valor_hora):
        self.idpro=idpro
        self.nombre=nombre
        self.abrebiatura=abrebiatura
        self.metrica=metrica
        self.tipo=tipo
        self.valor_hora=valor_hora