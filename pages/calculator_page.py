from typing import Self

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """Page Object страницы калькулятора."""

    DELAY_INPUT = (By.CSS_SELECTOR, "input#delay")
    RESULT_DIV = (By.CSS_SELECTOR, "div.screen")

    BUTTON_7 = (By.XPATH, "//span[normalize-space()='7']")
    BUTTON_8 = (By.XPATH, "//span[normalize-space()='8']")
    BUTTON_PLUS = (By.XPATH, "//span[normalize-space()='+']")
    BUTTON_EQUALS = (By.XPATH, "//span[normalize-space()='=']")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу калькулятора.

        :param driver: Экземпляр Selenium WebDriver.
        :return: Метод ничего не возвращает.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self, url: str) -> Self:
        """
        Открывает страницу калькулятора.

        :param url: URL страницы калькулятора.
        :return: Текущий экземпляр CalculatorPage.
        """
        self.driver.get(url)

        self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )

        return self

    def set_delay(self, value: str) -> Self:
        """
        Устанавливает задержку выполнения калькуляции.

        :param value: Значение задержки в виде строки.
        :return: Текущий экземпляр CalculatorPage.
        """
        delay_field = self.wait.until(
            EC.element_to_be_clickable(self.DELAY_INPUT)
        )

        delay_field.clear()
        delay_field.send_keys(value)

        return self

    def click_7(self) -> Self:
        """
        Нажимает кнопку с цифрой 7.

        :return: Текущий экземпляр CalculatorPage.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_7)
        ).click()

        return self

    def click_8(self) -> Self:
        """
        Нажимает кнопку с цифрой 8.

        :return: Текущий экземпляр CalculatorPage.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_8)
        ).click()

        return self

    def click_plus(self) -> Self:
        """
        Нажимает кнопку сложения.

        :return: Текущий экземпляр CalculatorPage.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_PLUS)
        ).click()

        return self

    def click_equals(self) -> Self:
        """
        Нажимает кнопку равно.

        :return: Текущий экземпляр CalculatorPage.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_EQUALS)
        ).click()

        return self

    def wait_result(self, expected_text: str) -> Self:
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        :param expected_text: Ожидаемый текст результата.
        :return: Текущий экземпляр CalculatorPage.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                self.RESULT_DIV,
                expected_text
            )
        )

        return self

    def get_result_text(self) -> str:
        """
        Возвращает текст, отображаемый на экране калькулятора.

        :return: Текст результата без пробелов в начале и конце.
        """
        result = self.wait.until(
            EC.visibility_of_element_located(self.RESULT_DIV)
        )

        return result.text.strip()
