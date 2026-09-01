import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)

    driver.implicitly_wait(0)
    yield driver
    driver.quit()


def test_shop_checkout(driver):
    url = "https://www.saucedemo.com/"
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    cart_button = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    cart_button.click()

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name_input = driver.find_element(By.ID, "first-name")
    first_name_input.send_keys("Никита")

    last_name_input = driver.find_element(By.ID, "last-name")
    last_name_input.send_keys("Пидунов")

    postal_code_input = driver.find_element(By.ID, "postal-code")
    postal_code_input.send_keys("123456")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    total_element = wait.until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, ".summary_total_label"))
    )
    total_text = total_element.text

    assert total_text == "Total: $58.29", f"Ожидалась сумма $58.29, получено: {
        total_text}"
