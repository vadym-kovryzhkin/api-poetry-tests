# API tests for PoetryDB API

# Usage

## Docker execution

TBD

## Local Development environment

### Requirements

1. Install Python 3.10+

### Tests execution

1. Create virtualenv in the project folder: `virtualenv venv`
1. Install dependencies: `pip install -r requirements.txt`
1. Activate virtualenv:
    - Unix: `source venv/bin/activate`
    - Windows: `.\venv\Scripts\activate`
1. Run tests: `pytest -v -s`

### Test Cases:

| Test Case                                          | Objective                                                                              | Endpoint                                       | Verification Steps                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Retrieve All Poems by a Specific Author**        | Verify that the API returns all poems by a given author when using the `author` field. | `/author/<author>`                             | - Validate response status code to make sure the server responded with the correct HTTP status code<br> - Each poem’s `author` field matches "<Author Name>", since this is what we have requested and we want to make sure we got results for a correct author. <br> - Validate the JSON schema of the response, to make sure that it is in the correct format and contains all the necessary items with valid data types. 
|
| **Retrieve Specific Poem by Title**                | Verify that the API can return a specific poem’s content by title.                     | `/title/<title>/<output field>,<output field>` | - Validate response status code to make sure the server responded with the correct HTTP status code<br> - Since we clearly know we get only 1 poem - we should get exactly 1 poem by its name. <br> - Verify `title` contains correct poem name we requested. <br> - Validate the JSON schema of the response, to make sure that it is in the correct format and contains all the necessary items with valid data types.    |
| **Retrieve Random Poems with a Specificed Number** | Ensure the API returns a specified number of random poems.                             | `/random/<random count>`                       | - Validate response status code to make sure the server responded with the correct HTTP status code<br> - Check we got a specific number of poems based on a requested amount. <br> - Validate the JSON schema of the response, to make sure that it is in the correct format and contains all the necessary items with valid data types.                                                                                   |


### What else can be improved
1. .env usage
1. Logs
1. Dockerfile configuration
1. Tests execution command (e.g. using bash)
1. Test data arrangement
1. Non *unix support
1. Parallel support
1. poetry usage instead of pip
1. linting 