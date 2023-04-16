from db import db

class TagModel(db.Model):
    __tablename__="tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    loja_id = db.Column(db.Integer, db.ForeignKey("lojas.id"), nullable=False)
    
    loja = db.relationship("LojaModel", back_populates="tags")