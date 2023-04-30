import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import LojaModel
from schemas import LojaSchema

blp = Blueprint("lojas", __name__, description="Operações da loja")


@blp.route("/lojas/<int:loja_id>")
class Loja(MethodView):
# Busca loja especifica pelo id
    @blp.response(200, LojaSchema)
    def get(self, loja_id):
        loja = LojaModel.query.get_or_404(loja_id)
        return loja
    
# Deleta loja
    def delete(self, loja_id):
        loja = LojaModel.query.get_or_404(loja_id)
        db.session.delete(loja)
        db.session.commit()
        return {"message": "Loja deletada"}, 200
    
# Todas as lojas
@blp.route("/lojas")
class StoreList(MethodView):
    @blp.response(200, LojaSchema(many=True))
    def get(self):
        return LojaModel.query.all()

# Cria loja
# Linha de código que fará a validação dos dados
@blp.arguments(LojaSchema)
# Adicionando uma nova loja ao sistema #01
@blp.response(201, LojaSchema)
def post(self, loja_data):
        loja = LojaModel(**loja_data)

        try:
            db.session.add(loja)
            db.session.commit()
        except IntegrityError:
            abort(400,message="Esse nome já está sendo utilizado por outra loja")

        except SQLAlchemyError:
            abort(500,message="Erro ao tentar criar a loja")
            
        return loja
