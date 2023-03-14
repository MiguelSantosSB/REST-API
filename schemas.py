from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    preco = fields.Str(required=True)

class PlainLojaSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True) 

class ItemUpdateSchema(Schema):
    name = fields.Str()
    preco = fields.Str()

class ItemSchema(PlainItemSchema):
    loja_id = fields.Int(required=True, load_only=True)
    loja = fields.Nested(PlainLojaSchema(), dump_only=True)

class LojaSchema(PlainLojaSchema):
    itens = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
