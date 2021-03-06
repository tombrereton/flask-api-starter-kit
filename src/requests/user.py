from dataclasses import dataclass, field
import marshmallow_dataclass
from flask_marshmallow import Schema
from typing import List


@dataclass
class CreateUserRequest:
    UserName: str


CreateUserRequestSchema = marshmallow_dataclass.class_schema(CreateUserRequest, base_schema=Schema)


@dataclass
class CreateManyUsersRequest:
    Users: List[CreateUserRequest]


CreateManyUsersRequestSchema = marshmallow_dataclass.class_schema(CreateManyUsersRequest, base_schema=Schema)


@dataclass
class GetUserRequest:
    isSnakeCase: bool = field(default=False)


GetUserRequestSchema = marshmallow_dataclass.class_schema(GetUserRequest, base_schema=Schema)
