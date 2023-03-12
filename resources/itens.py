import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import itens

from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Itens", __name__, decription="Operações dos Itens")


@blp.route("/itens/<string:item_id>")
class Item(MethodView):
# procura item especifico
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return itens[item_id]
        except KeyError:
            abort(404,menssage="Loja não encontrada.")
# deleta item
    def delete(self, item_id):
        try:
            del itens[item_id]
            return {"mensage": "Item DELETADO com sucesso."}
        except KeyError:
            abort(404,menssage= "Item não encontrado.")
# modifica item
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        try:
            item = itens[item_id]
            
            item |= item_data

            return item
        except KeyError:
            abort(404, message= "Item não encontrado")

@blp.route("/itens")
class ItemList(MethodView):
# Mostra todos os itens
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return itens.values()

# Cria item
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        for item in itens.values():
            if (item_data["name"] == itens["name"]
                and item_data["loja_id"] == itens["loja_id"]
                ):
                abort(404,menssage= "Loja não encontrada.")

        item_id = uuid.uuid4().hex 
        item = {**item_data, "id": item_id}
        itens[item_id] = item
        return item
