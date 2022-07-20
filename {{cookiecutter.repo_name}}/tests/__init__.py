import pytest

from {{cookiecutter.app_name}} import create_app
{%- if cookiecutter.use_postgres == "yes" %}
from {{cookiecutter.app_name}} import db
{%- endif %}


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("{{cookiecutter.app_name}}.config.TestingConfig")
    with app.app_context():
        yield app  # testing happens here

{%- if cookiecutter.use_postgres == "yes" %}
@pytest.fixture(scope="module")
def test_database():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()
{%- endif %}
