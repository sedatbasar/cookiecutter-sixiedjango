import pytest
{%- if cookiecutter.use_graphql == "y" %}
from strawberry_django.test.client import TestClient
{%- endif %}

from {{ cookiecutter.project_slug }}.users.models import User
from {{ cookiecutter.project_slug }}.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


{% if cookiecutter.use_graphql == "y" -%}
@pytest.fixture
def graphql_client() -> TestClient:
    return TestClient("/graphql/")
{%- endif %}
