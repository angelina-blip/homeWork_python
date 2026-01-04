from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = None

    def proceed_to_checkout(self):
        self.checkout_button = self.driver.find_element(By.CSS_SELECTOR, "#checkout")
        self.checkout_button.click()