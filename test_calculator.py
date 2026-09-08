import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(10)
    yield drv
    drv.quit()


def test_calculator_7_plus_8(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    page = CalculatorPage(driver).open(url)

    page.set_delay("45")

    page.click_7().click_plus().click_8().click_equals()

    page.wait_result("15")

    assert page.get_result_text() == "15", "Результат должен быть 15"
