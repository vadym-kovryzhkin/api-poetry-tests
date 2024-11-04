import jsonschema

from api_services.title_api_service import TitleApiService
from json_schemas import title_schema


def test_should_get_poem_by_title():
    # Arrange
    title_name = "Ozymandias"

    # Act
    res = TitleApiService().get_poem_by_title(title_name)
    poems = res.json()

    # Assert
    assert res.status_code == 200
    jsonschema.validate(poems, title_schema.TITLE_SCHEMA_GET)
    # we expect only one poem to be returned
    assert len(poems) == 1, "Expected only one poem to be returned"
    assert poems[0]["title"] == title_name, f"Title mismatch in poem: {poems[0]}"
