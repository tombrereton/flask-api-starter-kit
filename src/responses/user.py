from dataclasses import field, dataclass
from typing import List

import marshmallow_dataclass
from marshmallow import Schema


@dataclass
class UserResponse:
    UserName: str


UserResponseSchema = marshmallow_dataclass.class_schema(UserResponse, base_schema=Schema)


@dataclass
class AllUsersResponse:
    Users: List[UserResponse] = field(default_factory=list)


AllUsersResponseSchema = marshmallow_dataclass.class_schema(AllUsersResponse)
