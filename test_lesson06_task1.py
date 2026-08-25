from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_button = wait.until(
     EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#start button"))
    )
    start_button.click()

    hello_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )
    actual_text = hello_element.text

    driver.save_screenshot("dynamic_loading_screenshot.png")

    assert actual_text == "Hello World!", "Text mismatch"

    driver.quit()
