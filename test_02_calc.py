import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(0)
    yield driver
    driver.quit()


def test_calculator_result(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    driver.get(url)

    wait = WebDriverWait(driver, 60)

    # Вводим задержку 45 секунд
    delay_input = wait.until(
        EC.visibility_of_element_located((By.ID, "delay"))
    )
    driver.execute_script(
        "arguments[0].value = '45'; arguments[0].dispatchEvent("
        "new Event('change'));",
        delay_input
    )

    buttons = ["7", "+", "8", "="]
    for button in buttons:
        driver.find_element(
            By.XPATH,
            f"//span[contains(@class, 'btn') and text()='{button}']"
        ).click()

    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )

    screen = driver.find_element(By.CSS_SELECTOR, "div.screen")
    assert screen.text == "15", f"Ожидался результат 15, получено: {
        screen.text}"
