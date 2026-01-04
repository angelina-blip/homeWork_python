from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)
        # Локаторы
        self.locators = {
            'delay_input': (By.ID, "delay"),
            'result_display': (By.CSS_SELECTOR, ".screen"),
            'button_template': "//span[text() = '{}']"
        }

    def open(self, url):
        self.driver.get(url)

    def set_delay(self, seconds):
        delay_element = self.driver.find_element(*self.locators['delay_input'])
        delay_element.clear()
        delay_element.send_keys(str(seconds))

    def click_button(self, button_text):
        xpath = self.locators['button_template'].format(button_text)
        self.driver.find_element(By.XPATH, xpath).click()

    def wait_for_result(self, expected_text):
        self.wait.until(
            EC.text_to_be_present_in_element(self.locators['result_display'], expected_text)
        )