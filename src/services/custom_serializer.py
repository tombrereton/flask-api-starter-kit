from dataclasses_serialization.serializer_base import noop_serialization, noop_deserialization, dict_serialization, \
    dict_deserialization, list_deserialization, Serializer


def snake_to_pascal_case(obj):
    parts = iter(obj.split("_"))
    return "".join(i.title() for i in parts)


def snake_to_pascal_case_list_map(obj):
    obj_dict = obj.__dict__
    key = next(iter(obj_dict))
    parts = iter(key.split('_'))
    new_key = "".join(i.title() for i in parts)
    return {new_key: obj_dict.get(key)}


JSONSerializer = Serializer(
    serialization_functions={
        dict: lambda dct: dict_serialization(dct, key_serialization_func=snake_to_pascal_case,
                                             value_serialization_func=JSONSerializer.serialize),
        list: lambda lst: list(map(snake_to_pascal_case_list_map, lst)),
        (str, int, float, bool, type(None)): noop_serialization
    },
    deserialization_functions={
        dict: lambda cls, dct: dict_deserialization(cls, dct, key_deserialization_func=JSONSerializer.deserialize,
                                                    value_deserialization_func=JSONSerializer.deserialize),
        list: lambda cls, lst: list_deserialization(cls, lst, deserialization_func=JSONSerializer.deserialize),
        (str, int, float, bool, type(None)): noop_deserialization
    }
)
