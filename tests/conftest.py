import pytest
from flaskr import create_app

@pytest.fixture
def client():
    app = create_app(test_config={
        'TESTING': True,
    })
    app_client = app.test_client()
    yield app_client
