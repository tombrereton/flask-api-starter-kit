# Flask API Starter Kit

- Sample API focusing on Separation of Concerns for testability.
- This API uses Pascal Case (or Camel Case) for the JSON endpoints.
- Swagger docs at http://localhost/apidocs 
- Based on [https://github.com/bajcmartinez/flask-api-starter-kit](https://github.com/bajcmartinez/flask-api-starter-kit)

## Design
This is loosely based off clean architecture (onion architecture, ports & adapters).
It is important to keep the data access within the Repository classes/modules so they
can be mocked out for easy testing. This means unit tests can cover the majority of the application (the domain)
and the integration tests can target the application boundary and some happy path scenarious.

### Directory Structure

#### `root` Folder
- `Pipfile`: replaces requirement.txt, see below for use
- `.env`: environment variables, these are loaded into memory in the `config.py`


#### `src` Folder
- `app.py`: This file creates the Flask app (similar to `Startup.cs` in .NET Core)
- `config.py`: This file stores the config and reads in environment variables (similar to `appsettings.json` in .NET Core)
- `schemas`: are used by the endpoints to deserialize/serialize and validate request parameters/bodies
- `dtos`: are used for internal (i.e. domain, in-memory) data transfer
- `dtos`: can also be serialised into CamelCase using the `custom_serializer.py`
- `models` or `entities`: add this folder for objects to store in database
- `repositories`: to handle data persistence
- `services`: for modules & classes that don't belong in Repositories

#### `test` Folder
- Mirrors the src folders 

## Dependencies

- [flask](https://palletsprojects.com/p/flask/): Python server of choise
- [flasgger](https://github.com/flasgger/flasgger): Used to generate the swagger documentation
- [flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/): Used for Pascal to Snake case converter and to define Swagger Schema
- [apispec](https://apispec.readthedocs.io/en/latest/): Required for the integration between marshmallow and flasgger
- [dataclass-serialization](https://github.com/madman-bob/python-dataclasses-serialization): Used to convert Snake Case dataclasses (DTOs) to Pascal Case

## Dev Dependencies
- [pytest](https://docs.pytest.org/en/6.2.x/): Testing framework of choice
- [assertpy](https://github.com/assertpy/assertpy): Used for fluent assertions 

## Set Up

1. Check out the code
2. Install requirements
    ```
    python3 -m venv venv
    source venv/bin/active
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```
3. Start the server with:
    ```
    python -m flask run
    ```
   
5. Visit http://localhost/api/ for the home api

6. Visit http://localhost/apidocs for the swagger documentation
   
## Tests

The code is covered by tests, to run the tests please execute

```
pipenv run python -m pytest
```


## Development
Some useful `pipenv` commands

```
pipenv install <package_name> # for any version
pipenv install requests~=1.2 # for specific version
```

Install development (test) dependencies
```
pipenv install <package_name> -d
```

Open Shell and Exit
```
pipenv shell
python --version
exit
```


