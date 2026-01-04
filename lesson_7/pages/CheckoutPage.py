from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = None
        self.last_name_field = None
        self.postal_code_field = None
        self.continue_button = None
        self.total_label = None

    def fill_form_data(self, first_name, last_name, postal_code):
        self.first_name_field = self.driver.find_element(By.CSS_SELECTOR, "#first-name")
        self.first_name_field.send_keys(first_name)
        self.last_name_field = self.driver.find_element(By.CSS_SELECTOR, "#last-name")
        self.last_name_field.send_keys(last_name)
        self.postal_code_field = self.driver.find_element(By.CSS_SELECTOR, "#postal-code")
        self.postal_code_field.send_keys(postal_code)
        self.continue_button = self.driver.find_element(By.CSS_SELECTOR, "#continue")
        self.continue_button.click()

    def get_total_price(self):
        wait = WebDriverWait(self.driver, 10)
        self.total_label = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-test="total-label"]')))
        return self.total_label.text.split(": ")[1].strip()