import sys
import os

# Путь к корню проекта для правильных импортов
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import requests
import allure

from config.env_config import BASE_URL
from test.config.test_data import HEADERS


@pytest.mark.api
@allure.title("Поиск с пустым значением query=''")
@allure.story("Поиск фильмов с пустым параметром 'query'")
def test_search_empty_query():
    params = {"query": ""}
    with allure.step(f"Отправляем GET запрос на {BASE_URL} с query=''"):
        response = requests.get(BASE_URL, headers=HEADERS, params=params)

    with allure.step("Проверяем, что статус ответа 200"):
        assert response.status_code == 200

    with allure.step("Проверяем, что ответ содержит фильм '1+1'"):
        json_data = response.json()
        assert "docs" in json_data
        assert any(film.get("name") == "1+1" for film in json_data["docs"])


@pytest.mark.api
@allure.title("Поиск по произвольному набору символов query='vdvdfbvfd'")
@allure.story("Поиск с несуществующим непонятным ключевым словом")
def test_search_random_string():
    params = {"query": "vdvdfbvfd"}
    with allure.step(f"Отправляем GET запрос с query=vdvdfbvfd"):
        response = requests.get(BASE_URL, headers=HEADERS, params=params)

    with allure.step("Проверяем статус 200"):
        assert response.status_code == 200

    with allure.step("Проверяем, что 'docs' пуст и total=0"):
        json_data = response.json()
        assert json_data.get("docs") == []
        assert json_data.get("total") == 0


@pytest.mark.api
@allure.title("Поиск с неправильно написанным названием query='аввгст'")
@allure.story("Поиск с частично невалидным (опечатка) названием")
def test_search_misspelled_name():
    params = {"query": "аввгст"}
    with allure.step(f"Отправляем GET запрос с query=аввгст"):
        response = requests.get(BASE_URL, headers=HEADERS, params=params)

    with allure.step("Проверяем статус 200"):
        assert response.status_code == 200

    with allure.step("Проверяем, что в ответе содержится фильм 'Матрица'"):
        json_data = response.json()
        names = [film.get("name") for film in json_data.get("docs", [])]
        assert "Матрица" in names


@pytest.mark.api
@allure.title("Поиск фильма используя спецсимволы query=';)?)%%'")
@allure.story("Поиск с использованием специальных символов")
def test_search_special_chars():
    params = {"query": ";)?)%%"}
    with allure.step(f"Отправляем GET запрос с query=';)?)%%'"):
        response = requests.get(BASE_URL, headers=HEADERS, params=params)

    with allure.step("Проверяем статус 200"):
        assert response.status_code == 200

    with allure.step("Проверяем, что в ответе содержится фильм '1+1'"):
        json_data = response.json()
        names = [film.get("name") for film in json_data.get("docs", [])]
        assert "1+1" in names


@pytest.mark.api
@allure.title("Попытка поиска без токена query='пианист'")
@allure.story("Проверка ответа при отсутствии токена авторизации")
def test_search_without_token():
    params = {"query": "пианист"}
    with allure.step(f"Отправляем GET запрос на {BASE_URL} без токена с query='пианист'"):
        response = requests.get(BASE_URL, params=params)  # без headers!

    with allure.step("Проверяем, что статус ответа 401 Unauthorized"):
        assert response.status_code == 401

    with allure.step("Проверяем сообщение об отсутствии токена"):
        json_data = response.json()
        assert json_data.get("message") == "В запросе не указан токен!"
        assert json_data.get("error") == "Unauthorized"