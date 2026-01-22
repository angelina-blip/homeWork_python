import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

@allure.feature("Cart Page")
class CartPage:
    """
    Класс, моделирующий страницу корзины.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы корзины.

        :param driver: WebDriver - драйвер Selenium.
        """
        self.driver = driver

    @allure.step("Процесс оформления заказа: нажать кнопку 'Checkout'")
    def proceed_to_checkout(self) -> None:
        """
        Переходит к оформлению заказа.

        :return: None
        """
        checkout_button = self.driver.find_element(By.CSS_SELECTOR, "#checkout")
        checkout_button.click()