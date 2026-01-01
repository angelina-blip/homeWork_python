import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_validation():
    driver = webdriver.Edge()
    driver.maximize_window()

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        fields = {
            'first-name': 'Иван',
            'last-name': 'Петров',
            'address': 'Ленина, 55-3',
            'e-mail': 'test@skypro.com',
            'phone': '+7985899998787',
            'city': 'Москва',
            'country': 'Россия',
            'job-position': 'QA',
            'company': 'SkyPro'
        }

        for name, value in fields.items():
            driver.find_element(By.NAME, name).send_keys(value)

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

        zip_class = driver.find_element(By.ID, "zip-code").get_attribute("class")
        assert "alert-danger" in zip_class, f"Zip code не красный! Классы: {zip_class}"

        success_ids = [
            "first-name", "last-name", "address", "city",
            "country", "e-mail", "phone", "job-position", "company"
        ]

        for field_id in success_ids:
            field_class = driver.find_element(By.ID, field_id).get_attribute("class")
            assert "alert-success" in field_class, f"Поле {field_id} не зеленое! Классы: {field_class}"

        print("\nТест успешно пройден!")

    finally:
        driver.quit()