import pytest
import requests
import uuid

# Базовый URL API
BASE_URL = "https://ru.yougile.com"
API_TOKEN = "TtK2+WJYJlG0+SbqLygJjxNaC-Ar01l0HeWUNsJhxj+2RIGG1BI3qjUIJmFC3G3Z"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

@pytest.fixture
def project_id():
    payload = {"title": f"Тестовый проект {uuid.uuid4()}"}
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS, json=payload)

    if response.status_code != 201:
        pytest.fail(f"Не удалось подготовить данные для теста: {response.text}")

    new_id = response.json().get("id")
    yield new_id

    requests.delete(f"{BASE_URL}/api-v2/projects/{new_id}", headers=HEADERS)

# --- ТЕСТЫ POST (Создание) ---

def test_create_project_positive():
    """Позитивный тест на создание проекта (201 Created)"""
    payload = {
        "title": f"Новый проект {uuid.uuid4()}"
    }
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS, json=payload)

    assert response.status_code == 201
    data = response.json()
    assert "id" in data

    # Сразу удалим за собой созданный проект
    requests.delete(f"{BASE_URL}/api-v2/projects/{data['id']}", headers=HEADERS)

def test_create_project_negative_empty_title():
    """Негативный тест: создание проекта без обязательного поля title (400 Bad Request)"""
    payload = {
        "description": "Описание без названия"
    }
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS, json=payload)

    # API должно вернуть 400, так как title обязателен
    assert response.status_code == 400

# --- ТЕСТЫ PUT (Обновление) ---

def test_update_project_positive(project_id):
    """Позитивный тест на обновление названия (200 OK)"""
    update_payload = {"title": "Обновленное название 2026"}
    url = f"{BASE_URL}/api-v2/projects/{project_id}"
    response = requests.put(url, headers=HEADERS, json=update_payload)

    assert response.status_code == 200
    assert response.json().get("id") == project_id

def test_update_project_negative_not_found():
    """Негативный тест: обновление несуществующего проекта (404 Not Found)"""
    invalid_id = str(uuid.uuid4())
    url = f"{BASE_URL}/api-v2/projects/{invalid_id}"
    response = requests.put(url, headers=HEADERS, json={"title": "Test"})

    assert response.status_code == 404

# --- ТЕСТЫ GET (Получение) ---

def test_get_project_positive(project_id):
    """Позитивный тест на получение данных проекта (200 OK)"""
    url = f"{BASE_URL}/api-v2/projects/{project_id}"
    response = requests.get(url, headers=HEADERS)

    assert response.status_code == 200
    assert "title" in response.json()

def test_get_project_negative_invalid_uuid():
    """Негативный тест: получение проекта по некорректному формату ID (400 или 404)"""
    url = f"{BASE_URL}/api-v2/projects/not-a-uuid"
    response = requests.get(url, headers=HEADERS)

    # Обычно API возвращает 400 на невалидный формат строки или 404
    assert response.status_code in [400, 404]