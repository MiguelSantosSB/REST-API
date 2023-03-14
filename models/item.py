from db import db

class ItemModel(db.Model):
    __tablbename__="itens"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    preco = db.Column(db.Float(precison=2), unique=False, nullable=False)
    loja_id = db.Column(db.Integer, db.ForeingKey("lojas.id"), unique=False, nullable=False)
    loja = db.relationship("LojaModel", back_populates="itens")
