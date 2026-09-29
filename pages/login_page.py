from typing import TYPE_CHECKING
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Для избежания циклического импорта при типизации
if TYPE_CHECKING:
    from pages.inventory_page import InventoryPage


class LoginPage:
    """
    Класс страницы авторизации.

    Предоставляет методы для открытия страницы логина,
    ввода учётных данных и выполнения входа в систему.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации.

        :param driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы элементов страницы
        self.USERNAME_INPUT = (By.CSS_SELECTOR, "input#user-name")
        self.PASSWORD_INPUT = (By.CSS_SELECTOR, "input#password")
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, "input#login-button")

    def open(self, url: str) -> "LoginPage":
        """
        Открывает страницу авторизации по указанному URL.

        :param url:
          Адрес страницы для открытия (например, базовый URL приложения)
        :return: Экземпляр LoginPage для продолжения цепочки вызовов
        """
        self.driver.get(url)
        return self

    def login(self, username: str, password: str) -> "InventoryPage":
        """
        Выполняет вход в систему с указанными учётными данными.

        :param username: Имя пользователя для авторизации
        :param password: Пароль для авторизации
        :return: Экземпляр InventoryPage после успешного входа
        """
        # Ввод имени пользователя
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        ).send_keys(username)

        # Ввод пароля
        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        ).send_keys(password)

        # Нажатие кнопки входа
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

        # Возврат следующей страницы
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)
