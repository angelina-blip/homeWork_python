from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = None
        self.password_field = None
        self.login_button = None

    def open_login_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.username_field = self.driver.find_element(By.CSS_SELECTOR, '#user-name')
        self.username_field.send_keys(username)

    def enter_password(self, password):
        self.password_field = self.driver.find_element(By.CSS_SELECTOR, '#password')
        self.password_field.send_keys(password)

    def submit_login(self):
        self.login_button = self.driver.find_element(By.CSS_SELECTOR, '#login-button')
        self.login_button.click()