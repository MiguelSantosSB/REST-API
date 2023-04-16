from flask.views import MethodView
from flask_smorest import Blueprint,abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import TagModel, LojaModel
from schemas import TagSchema

blp = Blueprint("Tags", "tags", description="Operations on tags")

@blp.route("/loja/<string:loja_id>/tag")
class TagsInLoja(MethodView):
    @blp.response(200, TagSchema(many=True))
    def get(self, loja_id):
        loja = LojaModel.query.get_or_404(loja_id)

        return loja.tag.all()

@blp.arguments(TagSchema)
@blp.response(201, TagSchema)
def post(self, tag_data, loja_id):
    # if TagModel.query.filter(TagModel.loja_id == loja_id, TagModel.name == tag_data["name"]).first():
    #     abort(400, message="A tag with that name alredy exist in that loja")
    tag = TagModel(**tag_data, loja_id=loja_id)

    try:
        db.session.add(tag)
        db.session.commit()
    except SQLAlchemyError as e:
        abort(500, message=str(e))

    return tag

@blp.route("/tag/<string:tag_id>")
class Tag(MethodView):
    @blp.response(200, TagSchema)
    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag





