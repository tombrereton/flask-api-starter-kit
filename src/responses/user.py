from dataclasses import dataclass
import marshmallow_dataclass


@dataclass
class UserResponse:
    UserName: str


UserResponseSchema = marshmallow_dataclass.class_schema(UserResponse)
