import jsonschema
from json_schemas import author_schema
from api_services.author_api_service import AuthorApiService


def test_should_get_poem_by_author():
    # Arrange
    author_name = "Emily Dickinson"

    # Act
    res = AuthorApiService().get_poems_by_author(author_name)
    poems = res.json()

    # Assert
    assert res.status_code == 200
    jsonschema.validate(poems, author_schema.AUTHOR_SCHEMA_GET)
    for poem in poems:
        assert poem["author"] == author_name, f"Author mismatch in poem: {poem}"
