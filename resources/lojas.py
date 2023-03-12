import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import lojas

blp = Blueprint("lojas", __name__, decription="Operações da loja")


@blp.route("/lojas/<string:loja_id>")
class Loja(MethodView):
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
    def get(self):
        return {"lojas": list(lojas.values())}
    
# Adicionando uma nova loja ao sistema #01
def post(self):
# sistema que irá impedir a criação de lojas com o mesmo nome
    loja_data = request.get_json()
    if "name" not in loja_data:
        abort(400,mensage="Bad request. Ensure 'name' is included in JSON paylod.")
    
    for loja in lojas.values():
        if loja_data["name"] == loja["name"]:
            abort(400, mensage="Essa loja já existe.")
    loja_id = uuid.uuid4().hex 
    loja = {**loja_data, "id": loja_id}
    lojas[loja_id] = loja
    return loja, 201
