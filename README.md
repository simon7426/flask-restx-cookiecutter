# Flask Restx Cookiecutter

This is a cookiecutter to rapidly build a flask restx project with additional support to enable sqlalchemy, pymongo, celery if needed. With this setup, it is very easy to start a flask project with restx integrated. Only thing the user needs to do is start writing APIs.

## Installation

```code
cookiecutter https://github.com/simon7426/flask-restx-cookiecutter.git
```

It will ask you some basic questions before setting up the project. After it is done, cd into the newly created directory and run 

```code
poetry install
poetry export -f requirements.txt --output requirements.txt --without-hashes
make format
make lint
```

The project is now ready to use. Start the server with `make server`.
Test the project with `make tox`. Or run a short test with `make test`.

## Pre-Commit

This cookiecutter also contains a pre-commit-config file. After initializing the git repo, install the hooks with

```code
poetry run pre-commit install
```
