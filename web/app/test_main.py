"""
Example PyTest unit test
"""

from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    """
    Example PyTest unit test for a FastAPI route
    :return: None
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
