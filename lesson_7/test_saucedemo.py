import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_saucedemo_purchase(browser):
    login_page = LoginPage(browser)
    products_page = ProductsPage(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)

    # Открываем страницу авторизации
    login_page.open_login_page()

    # Авторизуемся
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.submit_login()

    # Добавляем товары в корзину
    products_page.add_product_to_cart("Backpack")
    products_page.add_product_to_cart("Bolt T-Shirt")
    products_page.add_product_to_cart("Onesie")

    # Перейдем в корзину
    products_page.go_to_cart()

    # Оформляем заказ
    cart_page.proceed_to_checkout()

    # Заполняем данные
    checkout_page.fill_form_data("Angelina", "Tarasova", "456020")

    # Получаем итоговую сумму
    actual_total = checkout_page.get_total_price()

    # Проверяем итоговую сумму
    expected_total = "$58.29"
    assert actual_total == expected_total, f"Expected total amount to be ${expected_total}, but got ${actual_total}"