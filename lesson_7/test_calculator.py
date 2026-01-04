import pytest
from selenium import webdriver
from calculator_page import CalculatorPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator_with_page_object(browser):
    calculator = CalculatorPage(browser)
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    # Открытие страницы
    calculator.open(url)
    # Установка задержки
    calculator.set_delay(45)

    # Ввод последовательности кнопок
    for btn in ["7", "+", "8", "="]:
        calculator.click_button(btn)

    # Проверка результата
    calculator.wait_for_result("15")