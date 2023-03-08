from flask import Flask, request

app = Flask(__name__)

lojas = [
    {
        "name": "minha loja",
        "itens": [
            {
                "nome": "feijao",
                "preco": 6.32
            },
            {
               "nome": "arroz",
                "preco": 5.64 
            }
        ]
    }
]
# Criando o sistema de lojas
@app.get("/lojas")
def get_loja():
    return {"lojas": lojas}

# Adicionando uma nova loja ao sistema
@app.post("/lojas")
def create_loja():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "itens":[]}
    lojas.append(new_store)
    return new_store, 201

# Adicionando os itens da loja no banco
@app.post("/lojas/<string:name>/itens")
def create_item(name):
    request_data = request.get_json()
    for store in lojas:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "preco": request_data["preco"]}
            store["itens"].append(new_item)
            return new_item, 201
    return {"menssage": "Loja não encontrada"}, 404

# procura se a loja especifica está armazenada e se sim retorna a loja especifica
@app.get("/lojas/<string:name>")
def get_store(name):
    for store in lojas:
        if store["name"] == name:
            return store
    return {"menssage": "Loja não encontrada"}, 404

# procura se uma loja está armazenada e se sim irá retorma seus itens
@app.get("/lojas/<string:name>/itens")
def get_item_in_store(name):
    for store in lojas:
        if store["name"] == name:
            return {"itens": store["itens"]}
    return {"menssage": "Loja não encontrada"}, 404