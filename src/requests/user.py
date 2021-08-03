from dataclasses import dataclass, field
import marshmallow_dataclass


@dataclass
class CreateUserRequest:
    UserName: str


CreateUserRequestSchema = marshmallow_dataclass.class_schema(CreateUserRequest)


@dataclass
class GetUserRequest:
    isSnakeCase: bool = field(default=False)


GetUserRequestSchema = marshmallow_dataclass.class_schema(GetUserRequest)
