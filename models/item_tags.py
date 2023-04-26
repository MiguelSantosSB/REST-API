from db import db 

class ItemTags(db.Model):
    __tablename__ = "itens_tags"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("itens.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))