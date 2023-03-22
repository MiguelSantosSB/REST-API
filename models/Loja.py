from db import db

class LojaModel(db.Model):
    __tablename__="lojas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    itens = db.relationship("ItemModel", back_populates="lojas", lazy="dynamic", cascade="all, delete, delete-orphan")
