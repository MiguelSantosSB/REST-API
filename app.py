from flask import Flask

app = Flask(__name__)

lojas = [
    {
        "name": "minha loja",
        "itens": [
            {
                "nome": "arroz",
                "preco": 5.64,
                "nome": "feijao",
                "preco": 6.32,
            },
        ]
    }
]

@app.get("/lojas")
def get_loja():
    return {"lojas": lojas}