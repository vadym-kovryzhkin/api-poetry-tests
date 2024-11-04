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

| Test Case                                          | Objective                                                                              | Endpoint                                       | Verification Steps                                                                                         |
|----------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| **Retrieve All Poems by a Specific Author**        | Verify that the API returns all poems by a given author when using the `author` field. | `/author/<author>`                             | - Validate response status code to ensure it’s correct.  
                                                                                                           - Each poem’s `author` field matches "<Author Name>".  
                                                                                                           - Validate the JSON schema for correct format and data types. |
| **Retrieve Specific Poem by Title**                | Verify that the API can return a specific poem’s content by title.                     | `/title/<title>/<output field>,<output field>` | - Validate response status code for correctness.  
                                                                                                           - Ensure exactly 1 poem is returned.  
                                                                                                           - Verify `title` matches the requested poem.  
                                                                                                           - Validate JSON schema for correct format and data types. |
| **Retrieve Random Poems with a Specified Number**  | Ensure the API returns a specified number of random poems.                             | `/random/<random count>`                       | - Validate response status code for correctness.  
                                                                                                           - Check for a specific number of poems.  
                                                                                                           - Validate JSON schema for correct format and data types. |


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