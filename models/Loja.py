from db import db

class LojaModel(db.Model):
    __tablbename__="lojas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    itens = db.relationship("itemModel", back_populates="loja", lazy="dynamic")