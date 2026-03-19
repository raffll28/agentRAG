from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_index_serves_chat_page():
    r = client.get("/")
    assert r.status_code == 200
    assert "text/html" in r.headers.get("content-type", "")
    assert b"agentRAG" in r.content


def test_static_css():
    r = client.get("/static/css/chat.css")
    assert r.status_code == 200


@patch("app.main.run_agent", return_value="mocked reply")
def test_post_ask(mock_run):
    r = client.post("/ask", json={"q": "hello"})
    assert r.status_code == 200
    assert r.json() == {"response": "mocked reply"}
    mock_run.assert_called_once_with("hello")


@patch("app.main.run_agent", return_value="x")
def test_get_ask(mock_run):
    r = client.get("/ask", params={"q": "hi"})
    assert r.status_code == 200
    assert r.json() == {"response": "x"}


def test_post_ask_empty_validation():
    r = client.post("/ask", json={"q": ""})
    assert r.status_code == 422
