import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from db import lojas

from schemas import LojasSchema

blp = Blueprint("lojas", __name__, decription="Operações da loja")


@blp.route("/lojas/<string:loja_id>")
class Loja(MethodView):
    @blp.response(200, LojasSchema)
    def get(self, loja_id):
        try:
            return lojas[loja_id]
        except KeyError:
            abort(404,menssage="Loja não encontrada.")

    def delete(self, loja_id):
        try:
            del lojas[loja_id]
            return {"mensage": "Loja DELETADO com sucesso."}
        except KeyError:
            abort(404,menssage= "Loja não encontrado.")

@blp.route("/lojas")
class StoreList(MethodView):
    @blp.response(200, LojasSchema(many=True))
    def get(self):
        return lojas.values()
    
# Linha de código que fará a validação dos dados
@blp.arguments(LojasSchema)
# Adicionando uma nova loja ao sistema #01
@blp.response(200, LojasSchema)
def post(self, loja_data):
    for loja in lojas.values():
        if loja_data["name"] == loja["name"]:
            abort(400, mensage="Essa loja já existe.")

    loja_id = uuid.uuid4().hex 
    loja = {**loja_data, "id": loja_id}
    lojas[loja_id] = loja
    return loja
