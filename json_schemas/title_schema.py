TITLE_SCHEMA_GET = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "lines": {
                "type": "array",
                "items": {"type": "string"}
            }
        },
        "required": ["title", "lines"]
    }
}
