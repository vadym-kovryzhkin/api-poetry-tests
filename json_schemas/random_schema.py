RANDOM_SCHEMA_GET = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "author": {"type": "string"},
            "linecount": {"type": "string"}
        },
        "required": ["title", "author", "linecount"]
    }
}
