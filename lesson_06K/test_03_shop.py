from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.implicitly_wait(10)

try:
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    # Добавление товаров
    products_buttons = [
        'button[name="add-to-cart-sauce-labs-backpack"]',
        'button[name="add-to-cart-sauce-labs-bolt-t-shirt"]',
        'button[name="add-to-cart-sauce-labs-onesie"]'
    ]

    for button_selector in products_buttons:
        driver.find_element(By.CSS_SELECTOR, button_selector).click()

    # Переход в корзину и оформление
    driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    # Заполнение данных
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Ангелина")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Тарасова")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("456020")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    # Проверка итоговой суммы
    wait = WebDriverWait(driver, 10)
    total_amount_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-test="total-label"]')))

    # Очищаем текст: получаем "Total: $58.29" -> берем вторую часть "$58.29"
    total_amount_text = total_amount_element.text.split(': ')[1]

    expected_total = "$58.29"
    assert total_amount_text == expected_total, f"Ожидалось: {expected_total}, получено: {total_amount_text}"

    print(f"Тест пройден! Итоговая сумма: {total_amount_text}")

finally:
    driver.quit()