import re

from dataclasses_serialization.serializer_base import noop_serialization, noop_deserialization, dict_serialization, \
    dict_deserialization, list_deserialization, Serializer


def to_snake_case(obj):
    regex = re.compile(r'(?<!^)(?=[A-Z])')
    replaced = re.sub(regex, '_', obj).lower()
    return replaced


def to_snake_case_map(obj):
    obj_dict = obj.__dict__
    key = next(iter(obj_dict))
    regex = re.compile(r'(?<!^)(?=[A-Z])')
    new_key = re.sub(regex, '_', key).lower()
    return {new_key: obj_dict.get(key)}


JSONSerializer = Serializer(
    serialization_functions={
        dict: lambda dct: dict_serialization(dct, key_serialization_func=to_snake_case,
                                             value_serialization_func=JSONSerializer.serialize),
        list: lambda lst: list(map(to_snake_case_map, lst)),
        (str, int, float, bool, type(None)): noop_serialization
    },
    deserialization_functions={
        dict: lambda cls, dct: dict_deserialization(cls, dct, key_deserialization_func=JSONSerializer.deserialize,
                                                    value_deserialization_func=JSONSerializer.deserialize),
        list: lambda cls, lst: list_deserialization(cls, lst, deserialization_func=JSONSerializer.deserialize),
        (str, int, float, bool, type(None)): noop_deserialization
    }
)
