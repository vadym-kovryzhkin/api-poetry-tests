import jsonschema
from json_schemas import random_schema
from api_services.random_api_service import RandomApiService


def test_should_get_random_poems_with_linecount():
    # Arrange
    random_count = 3  # can be any number. We avoid random to have deterministic tests

    # Act
    res = RandomApiService().get_random_poems_with_linecount(random_count)
    poems = res.json()

    # Assert
    assert res.status_code == 200
    jsonschema.validate(poems, random_schema.RANDOM_SCHEMA_GET)
    assert len(poems) == random_count, f"Expected {random_count} poems, but got {len(poems)}"
