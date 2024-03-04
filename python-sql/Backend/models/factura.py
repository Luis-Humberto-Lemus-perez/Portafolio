from utils.db import db
class Factura(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True )
    idencliente= db.Column(db.String(80))
    deudaconsumo=db.Column(db.Float)
    descripcion=db.Column(db.String(10000))
    categoria=db.Column(db.String(80))
    idconfi=db.Column(db.Integer)

    def __init__(self, idencliente, deudaconsumo, descripcion, categoria, idconfi):
        self.idencliente = idencliente
        self.deudaconsumo = deudaconsumo
        self.descripcion = descripcion
        self.categoria = categoria
        self.idconfi = idconfi