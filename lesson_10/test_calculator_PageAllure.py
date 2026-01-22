import pytest
import allure
from selenium import webdriver
from lesson_10.calculator_PageAllure import CalculatorPage

@pytest.fixture
def browser():
    # Инициализация браузера Chrome
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тест калькулятора: сложение 7 + 8")
@allure.description("Автоматизированный тест для проверки сложения 7 и 8 в калькуляторе с задержкой.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_with_page_object(browser):
    calculator = CalculatorPage(browser)
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    with allure.step("Открытие страницы калькулятора"):
        calculator.open(url)

    with allure.step("Установка задержки 45 секунд"):
        calculator.set_delay(45)

    with allure.step("Ввод числа '7'"):
        calculator.click_button("7")
    with allure.step("Нажатие кнопки '+'"):
        calculator.click_button("+")
    with allure.step("Ввод числа '8'"):
        calculator.click_button("8")
    with allure.step("Нажатие '='"):
        calculator.click_button("=")

    with allure.step("Проверка, что результат равен '15'"):
        calculator.wait_for_result("15")