import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator(browser):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    browser.get(url)

    delay_input = browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    buttons = ["7", "+", "8", "="]
    for button in buttons:
        xpath = f"//span[text() = '{button}']"
        browser.find_element(By.XPATH, xpath).click()

    wait = WebDriverWait(browser, 50)
    result = wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    
    assert result