from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_backpack_button = None
        self.add_bolt_tshirt_button = None
        self.add_onesie_button = None
        self.cart_link = None

    def add_product_to_cart(self, product_name):
        if product_name == "Backpack":
            self.add_backpack_button = self.driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-backpack"]')
            self.add_backpack_button.click()
        elif product_name == "Bolt T-Shirt":
            self.add_bolt_tshirt_button = self.driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-bolt-t-shirt"]')
            self.add_bolt_tshirt_button.click()
        elif product_name == "Onesie":
            self.add_onesie_button = self.driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-onesie"]')
            self.add_onesie_button.click()

    def go_to_cart(self):
        self.cart_link = self.driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]')
        self.cart_link.click()