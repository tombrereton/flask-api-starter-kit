from dataclasses import dataclass, field
import marshmallow_dataclass


@dataclass
class UserRequest:
    UserName: str


UserRequestSchema = marshmallow_dataclass.class_schema(UserRequest)
