from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Itens", __name__, description="Operações dos Itens")


@blp.route("/itens/<int:item_id>")
class Item(MethodView):
# procura item especifico
    @jwt_required()
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

# deleta item
    @jwt_required()
    def delete(self, item_id):
        jwt = get_jwt
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")

        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deletado"} 

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
# modifica item
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id)
        if item:    
            item.preco = item_data["preco"]
            item.name = item_data["name"]

        else:
            item = ItemModel(id = item_id,**item_data)

        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/itens")
class ItemList(MethodView):
# Mostra todos os itens
    @jwt_required()
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

# Cria item
    @jwt_required()
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Erro ao criar o item")
            
        return item
