from utils.db import db
class Consumos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idencliente= db.Column(db.String(80))
    ideninstancia= db.Column(db.String(80))
    tiempo= db.Column(db.Float)
    fechahora= db.Column(db.String(80))

    def __init__(self, idencliente, ideninstancia, tiempo, fechahora):
        self.idencliente = idencliente
        self.ideninstancia = ideninstancia
        self.tiempo = tiempo
        self.fechahora = fechahora