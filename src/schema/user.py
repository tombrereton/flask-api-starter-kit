from flask_marshmallow import Schema
from marshmallow import fields
from src.schema.pascal_mixin import PascalMixin


class UserSchema(Schema, PascalMixin):
    UserName = fields.Str(required=True)
