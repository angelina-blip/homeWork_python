import pytest
import allure
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_site_status():
    response = requests.get("https://www.kinopoisk.ru/")
    assert response.status_code == 200, "Сайт недоступен!"


@allure.title("Открытие расширенного поиска")
def test_open_extended_search(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.kinopoisk.ru/")

    with allure.step("Поиск кнопки 'Расширенный поиск'"):
        extended_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Расширенный поиск']")))
        assert extended_button.is_displayed()

    with allure.step("Клик по кнопке 'Расширенный поиск'"):
        extended_button.click()

    with allure.step("Проверяем появление формы расширенного поиска"):
        wait = WebDriverWait(driver, 10)  # Убедитесь, что у вас есть объект driver
        form = wait.until(EC.visibility_of_element_located((By.ID, "searchAdv")))
        assert form.is_displayed(), "Форма расширенного поиска не отображается"


@allure.title("Ввод цифр в поисковое поле")
def test_input_numbers_in_search_field(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.kinopoisk.ru/")

    # Кликаем на поле ввода
    search_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='kp_query']")))
    search_input.click()

    with allure.step("Вводим цифры в поле поиска"):
        search_input.clear()
        search_input.send_keys("123")
        search_input.send_keys(Keys.RETURN)

    # Проверка результатов
    wait.until(lambda d: d.current_url != "https://www.kinopoisk.ru/" or "ничего не найдено" in d.page_source)


@allure.title("Пустой поиск")
def test_empty_search_submit(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.kinopoisk.ru/")

    # Кликаем на поле ввода
    search_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='kp_query']")))
    search_input.click()

    with allure.step("Оставляем поле пустым и отправляем поиск"):
        search_input.clear()
        search_input.send_keys(Keys.RETURN)

    wait.until(lambda d: "ничего не найдено" in d.page_source or d.current_url != "https://www.kinopoisk.ru/")


@allure.title("Ввод случайных слов")
def test_random_text_search(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.kinopoisk.ru/")

    # Кликаем на поле ввода
    search_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='kp_query']")))
    search_input.click()

    with allure.step("Вводим текст 'qwertyuiop' и ищем"):
        search_input.clear()
        search_input.send_keys("qwertyuiop")
        search_input.send_keys(Keys.RETURN)

    wait.until(lambda d: "ничего не найдено" in d.page_source or d.current_url != "https://www.kinopoisk.ru/")