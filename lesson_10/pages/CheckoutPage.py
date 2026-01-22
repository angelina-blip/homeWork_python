import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

@allure.feature("Checkout Page")
class CheckoutPage:
    """
    Класс, моделирующий страницу оформления заказа.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы оформления заказа.

        :param driver: WebDriver - драйвер Selenium.
        """
        self.driver = driver

    @allure.step("Заполнить форму данных: {first_name} {last_name} {postal_code}")
    def fill_form_data(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму с данными покупателя и продолжает.

        :param first_name: str - имя
        :param last_name: str - фамилия
        :param postal_code: str - индекс
        :return: None
        """
        first_name_element = self.driver.find_element(By.CSS_SELECTOR, "#first-name")
        first_name_element.send_keys(first_name)

        last_name_element = self.driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name_element.send_keys(last_name)

        postal_code_element = self.driver.find_element(By.CSS_SELECTOR, "#postal-code")
        postal_code_element.send_keys(postal_code)

        continue_button = self.driver.find_element(By.CSS_SELECTOR, "#continue")
        continue_button.click()

    @allure.step("Получить итоговую цену")
    def get_total_price(self) -> str:
        """
        Получает финальную цену заказа.

        :return: str - цена
        """
        wait = WebDriverWait(self.driver, 10)
        total_label = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-test="total-label"]')))
        return total_label.text.split(": ")[1].strip()