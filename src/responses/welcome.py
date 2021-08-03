from dataclasses import dataclass
import marshmallow_dataclass
from flask_marshmallow import Schema


@dataclass
class WelcomeResponse:
    message: str


WelcomeResponseSchema = marshmallow_dataclass.class_schema(WelcomeResponse, base_schema=Schema)
