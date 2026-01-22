import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

@allure.feature("Login Page")
class LoginPage:
    """
    Класс, моделирующий страницу входа в приложение saucedemo.com.
    """

    def __init__(self, driver: WebDriver):
        """
        Конструктор страницы входа.

        :param driver: WebDriver - экземпляр драйвера Selenium.
        """
        self.driver = driver
        self.username_field: WebElement = None
        self.password_field: WebElement = None
        self.login_button: WebElement = None

    @allure.step("Открытие страницы входа")
    def open_login_page(self) -> None:
        """
        Открывает страницу входа.

        :return: None
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ввод имени пользователя: {username}")
    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя.

        :param username: str - логин пользователя.
        :return: None
        """
        self.username_field = self.driver.find_element(By.CSS_SELECTOR, '#user-name')
        self.username_field.send_keys(username)

    @allure.step("Ввод пароля: {password}")
    def enter_password(self, password: str) -> None:
        """
        Вводит пароль.

        :param password: str - пароль.
        :return: None
        """
        self.password_field = self.driver.find_element(By.CSS_SELECTOR, '#password')
        self.password_field.send_keys(password)

    @allure.step("Клик по кнопке входа")
    def submit_login(self) -> None:
        """
        Нажимает кнопку входа.

        :return: None
        """
        self.login_button = self.driver.find_element(By.CSS_SELECTOR, '#login-button')
        self.login_button.click()