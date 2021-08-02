from flask_marshmallow import Schema
from marshmallow.fields import Str


class WelcomeSchema(Schema):
    message = Str()


