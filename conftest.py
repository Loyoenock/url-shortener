import pytest
from urlshort import create_app

@pytest.fixture
def app():
    app = craete_app()
    yeild app

@pytest.fixture
def client(app):
    return app.test_client() 
