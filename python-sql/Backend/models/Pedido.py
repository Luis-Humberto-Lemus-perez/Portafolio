from utils.db import db

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idencate= db.Column(db.String(80))
    idenconfi= db.Column(db.String(80))
    iden= db.Column(db.String(80))
    numero= db.Column(db.Float)

    def __init__(self, idencate, idenconfi, iden, numero):
        self.idencate = idencate
        self.idenconfi = idenconfi
        self.iden = iden
        self.numero = numero