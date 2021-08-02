import re

from marshmallow import post_dump


def to_snake_case(s):
    regex = re.compile(r'(?<!^)(?=[A-Z])')
    replaced = re.sub(regex, '_', s).lower()
    return replaced


class PascalMixin:
    @post_dump
    def serialize(self, data, **kwargs):
        return {to_snake_case(key): value for key, value in data.items()}
