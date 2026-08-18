from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")

    sleep(2)
    driver.find_element(By.LINK_TEXT, "HTML Form").click()
    assert driver.current_url.endswith("/forms/post")

    sleep(2)
    driver.back()
    assert driver.current_url == "https://httpbin.qa-territory.online/"

    sleep(2)
    driver.quit()
