from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    sleep(3)

    url_before = driver.current_url

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Nikita")

    sleep(3)

    submit_button = driver.find_element(
        By.XPATH, "//button[normalize-space()='Submit order']"
    )
    submit_button.click()

    sleep(3)

    url_after = driver.current_url
    assert url_after != url_before, "URL не изменился после отправки формы"

    driver.quit()
