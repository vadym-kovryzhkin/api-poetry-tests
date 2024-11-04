AUTHOR_SCHEMA_GET = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "author": {"type": "string"},
            "lines": {
                "type": "array",
                "items": {"type": "string"}
            },
            "linecount": {"type": "string"}
        },
        "required": ["title", "author", "lines", "linecount"]
    }
}
