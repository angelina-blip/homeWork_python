from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CalculatorPage:
    """
    Страница калькулятора для автоматизированных тестов.
    """

    def __init__(self, driver):
        """
        Инициализация страницы.
        :param driver: WebDriver - экземпляр драйвера браузера.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)
        # Локаторы элементов
        self.locators = {
            'delay_input': (By.ID, "delay"),
            'result_display': (By.CSS_SELECTOR, ".screen"),
            'button_template': "//span[text()='{}']"
        }

    @allure.step('Открытие страницы по URL: {url}')
    def open(self, url):
        """
        Открывает страницу по URL.
        :param url: str
        """
        self.driver.get(url)

    @allure.step('Установка задержки: {seconds} секунд')
    def set_delay(self, seconds):
        """
        Устанавливает задержку.
        :param seconds: int
        """
        delay_element = self.driver.find_element(*self.locators['delay_input'])
        delay_element.clear()
        delay_element.send_keys(str(seconds))

    @allure.step('Нажатие кнопки: {button_text}')
    def click_button(self, button_text):
        """
        Нажимает кнопку с заданным текстом.
        :param button_text: str
        """
        xpath = self.locators['button_template'].format(button_text)
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step('Ожидание появления текста: "{expected_text}" на дисплее')
    def wait_for_result(self, expected_text):
        """
        Ожидает появления заданного текста в дисплее результата.
        :param expected_text: str
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.locators['result_display'], expected_text)
        )