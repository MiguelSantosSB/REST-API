import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import itens

blp = Blueprint("itens", __name__, decription="Operações dos Itens")


@blp.route("/itens/<string:item_id>")
class item(MethodView):
# procura item especifico
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
    def put(self, item_id):
        item_data = request.get_json()
        if(
            "preco" not in item_data 
            or "name" not in item_data
        ):
            abort(400, mensage="Bad request. Ensure 'preco', and 'name' are included in the JSON payload.")
    
        try:
            item = itens[item_id]
            item |= item_data

            return item
        except KeyError:
            abort(404, message= "Item não encontrado")

@blp.route("/itens")
class ItemList(MethodView):
# Mostra todos os itens
    def get(self):
        return {"itens": list(itens.values())}

# Cria item
    def post(self):
        item_data = request.get_json()

        if(
            "preco" not in item_data 
            or "loja_id" not in item_data 
            or "name" not in item_data
        ):
            abort(400, mensage="Bad request. Ensure 'preco', 'loja_id', and 'name' are included in the JSON payload.")
    
        if (item_data["name"] == itens["name"]
            and item_data["loja_id"] == itens["loja_id"]
            ):
            abort(404,menssage= "Loja não encontrada.")

        item_id = uuid.uuid4().hex 
        item = {**item_data, "id": item_id}
        itens[item_id] = item
        return item, 201
