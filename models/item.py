from sqlalchemy import ForeignKey
from db import db

class ItemModel(db.Model):
    __tablename__="itens"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    preco = db.Column(db.Float(precision=2), unique=False, nullable=False)
    
    loja_id = db.Column(db.Integer, db.ForeignKey("loja.id"), unique=False, nullable=False)
    loja = db.relationship("LojaModel", back_populates="itens")
    tags = db.relationship("TagModel", back_populates="itens", secondary="itens_tags")