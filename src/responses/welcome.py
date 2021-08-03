from dataclasses import dataclass
import marshmallow_dataclass


@dataclass
class WelcomeResponse:
    message: str


WelcomeResponseSchema = marshmallow_dataclass.class_schema(WelcomeResponse)
