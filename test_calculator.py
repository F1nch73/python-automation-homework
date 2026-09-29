from typing import Generator

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    """
    Создаёт и настраивает Chrome WebDriver.

    :yield: Экземпляр Chrome WebDriver.
    """
    options = Options()
    options.add_argument("--start-maximized")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)

    yield browser

    browser.quit()


@allure.title("Проверка сложения чисел 7 и 8")
@allure.description(
    "Тест проверяет, что калькулятор возвращает результат 15 "
    "при сложении чисел 7 и 8."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_7_plus_8(
    driver: WebDriver,
) -> None:
    """
    Проверяет результат сложения чисел 7 и 8.

    :param driver: Экземпляр Selenium WebDriver.
    :return: Метод ничего не возвращает.
    """
    url = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    with allure.step("Открыть страницу калькулятора"):
        page = CalculatorPage(driver).open(url)

    with allure.step("Установить задержку 45 секунд"):
        page.set_delay("45")

    with allure.step("Нажать кнопки 7 + 8"):
        (
            page
            .click_7()
            .click_plus()
            .click_8()
            .click_equals()
        )

    with allure.step("Дождаться появления результата 15"):
        page.wait_result("15")

    with allure.step("Проверить результат вычисления"):
        actual_result = page.get_result_text()

        assert actual_result == "15", (
            "Результат должен быть 15"
        )
