from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    preco = fields.Str(required=True)
    loja_id = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    preco = fields.Str()

class LojasSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)    
    