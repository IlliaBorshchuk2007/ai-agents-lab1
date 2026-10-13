
from fastapi.testclient import TestClient
from app.main import app, videos

client = TestClient(app)


def setup_function():
    videos.clear()


def test_create_video():
    response = client.post("/videos", json={
        "title": "Python",
        "topic": "цикли",
        "duration_minutes": 15
    })

    assert response.status_code == 201
    assert response.json()["title"] == "Python"


def test_get_videos():
    client.post("/videos", json={
        "title": "HTML",
        "topic": "форми",
        "duration_minutes": 20
    })

    response = client.get("/videos")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_invalid_duration():
    response = client.post("/videos", json={
        "title": "Python",
        "topic": "цикли",
        "duration_minutes": -5
    })

    assert response.status_code == 422
    assert len(videos) == 0


def test_missing_title():
    response = client.post("/videos", json={
        "topic": "цикли",
        "duration_minutes": 15
    })

    assert response.status_code == 422
    assert len(videos) == 0

from unittest.mock import patch


def test_ai_create_video():
    fake_result = {
        "title": "Python",
        "topic": "цикли",
        "duration_minutes": 15
    }

    with patch("app.main.extract_video", return_value=fake_result):
        response = client.post("/videos/ai", json={
            "text": "Відео Python, тема цикли, тривалість 15 хвилин"
        })

    assert response.status_code == 201
    assert response.json() == fake_result
    assert len(videos) == 1


def test_ai_missing_information():
    with patch("app.main.extract_video", return_value=None):
        response = client.post("/videos/ai", json={
            "text": "Відео Python, тема цикли"
        })

    assert response.status_code == 422
    assert len(videos) == 0
