import json

from jsonschema import validate


def test_schema():
    schema = {
        "type": "array",
        "properties": {
            "name": {"type": "string"},
            "gender": {"type": "string"},
            "address": {"type": "string"},
            "age": {"type": "number"},
            "books": {
                "type": "array",
                "properties": {
                    "title": {"type": "string"},
                    "author": {"type": "string"},
                    "pages": {"type": "number"},
                    "genre": {"type": "number"},
                },
            },
        },
    }

    with open("result.json", "r", encoding="utf-8") as reader:
        data = reader.read()
    validate(instance=json.loads(data), schema=schema)
