from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input#first-name")
        self.LAST_NAME_INPUT = (By.CSS_SELECTOR, "input#last-name")
        self.POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "input#postal-code")
        self.CONTINUE_BUTTON = (By.CSS_SELECTOR, "input#continue")
        self.TOTAL_LABEL = (By.CSS_SELECTOR, "div.summary_total_label")

    def fill_checkout_form(
            self, first_name: str, last_name: str, postal_code: str):
        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME_INPUT)
        ).send_keys(first_name)

        self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME_INPUT)
        ).send_keys(last_name)

        self.wait.until(
            EC.visibility_of_element_located(self.POSTAL_CODE_INPUT)
        ).send_keys(postal_code)

        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

        return self

    def get_total_text(self) -> str:
        total = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        )
        return total.text.strip()
