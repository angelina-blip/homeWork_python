import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

@allure.feature("Products Page")
class ProductsPage:
    """
    Класс, моделирующий страницу товаров.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы товаров.

        :param driver: WebDriver - драйвер Selenium.
        """
        self.driver = driver

    @allure.step("Добавить товар в корзину: {product_name}")
    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавляет определённый товар в корзину по имени.

        :param product_name: str - название товара ("Backpack", "Bolt T-Shirt", "Onesie").
        :return: None
        """
        if product_name == "Backpack":
            button = self.driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-backpack"]')
            button.click()
        elif product_name == "Bolt T-Shirt":
            button = self.driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-bolt-t-shirt"]')
            button.click()
        elif product_name == "Onesie":
            button = self.driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-onesie"]')
            button.click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """
        Перехходит в корзину.

        :return: None
        """
        cart_link = self.driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]')
        cart_link.click()