from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.USERNAME_INPUT = (By.CSS_SELECTOR, "input#user-name")
        self.PASSWORD_INPUT = (By.CSS_SELECTOR, "input#password")
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, "input#login-button")

    def open(self, url: str):
        self.driver.get(url)
        return self

    def login(self, username: str, password: str):
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        ).send_keys(username)

        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        ).send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

        return self
