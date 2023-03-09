import uuid
from flask import Flask, request
from flask_smorest import abort
from db import itens, lojas

app = Flask(__name__)

# lojas = [
#     {
#         "name": "minha loja",
#         "itens": [
#             {
#                 "nome": "feijao",
#                 "preco": 6.32
#             },
#             {
#                "nome": "arroz",
#                 "preco": 5.64 
#             }
#         ]
#     }
# ]


# Vendo o sistema de lojas #01
@app.get("/lojas")
def get_loja():
    return {"lojas": list(lojas.values())}

# Adicionando uma nova loja ao sistema #01
@app.post("/lojas")
def create_loja():
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

# Adicionando os itens da loja no banco #02
@app.post("/itens")
def create_item():
    item_data = request.get_json()

    if(
        "preco" not in item_data 
        or "loja_id" not in item_data 
        or "name" not in item_data
    ):
        abort(400, mensage="Bad request. Ensure 'preco', 'loja_id', and 'name' are included in the JSON payload.")
    
    if item_data["loja_id"] not in lojas:
        abort(404,menssage= "Loja não encontrada.")

    item_id = uuid.uuid4().hex 
    item = {**item_data, "id": item_id}
    itens[item_id] = item
    return item, 201

# Vendo o sistema de itens #02
@app.get("/itens")
def get_all_itens():
    return {"itens": list(itens.values())}

# procura se a loja especifica está armazenada e se sim retorna a loja especifica #03
@app.get("/lojas/<string:loja_id>")
def get_store(loja_id):
    try:
        return lojas[loja_id]
    except KeyError:
        abort(404,menssage="Loja não encontrada.")

# procura se uma loja está armazenada e se sim irá retorma seus itens #04
@app.get("/itens/<string:item_id>")
def get_item_in_store(item_id):
    try:
        return itens[item_id]
    except KeyError:
        abort(404,menssage= "Item não encontrado.")