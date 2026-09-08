from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        # Локаторы
        self.DELAY_INPUT = (By.CSS_SELECTOR, "input#delay")
        self.RESULT_DIV = (By.CSS_SELECTOR, "div.screen")

        # Кнопки калькулятора — span с текстом
        self.BUTTON_7 = (By.XPATH, "//span[normalize-space()='7']")
        self.BUTTON_8 = (By.XPATH, "//span[normalize-space()='8']")
        self.BUTTON_PLUS = (By.XPATH, "//span[normalize-space()='+']")
        self.BUTTON_EQUALS = (By.XPATH, "//span[normalize-space()='=']")

    def open(self, url: str):
        self.driver.get(url)
        self.wait.until(EC.presence_of_element_located(self.DELAY_INPUT))
        return self

    def set_delay(self, value: str):
        delay_field = self.wait.until(
            EC.element_to_be_clickable(self.DELAY_INPUT)
        )
        delay_field.clear()
        delay_field.send_keys(value)
        return self

    def click_7(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_7)
        ).click()
        return self

    def click_8(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_8)
        ).click()
        return self

    def click_plus(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_PLUS)
        ).click()
        return self

    def click_equals(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_EQUALS)
        ).click()
        return self

    def wait_result(self, expected_text: str):
        """Ждём, пока в div.screen появится ожидаемый текст."""
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT_DIV, expected_text)
        )
        return self

    def get_result_text(self) -> str:
        result = self.wait.until(
            EC.visibility_of_element_located(self.RESULT_DIV)
        )
        return result.text.strip()
