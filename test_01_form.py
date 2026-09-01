import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options)

    driver.implicitly_wait(0)
    yield driver
    driver.quit()


def test_form_validation(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    wait = WebDriverWait(driver, 15)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form")))

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Zip code оставляем пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3"
    )
    submit_button.click()

    zip_error = wait.until(
        EC.visibility_of_element_located((By.ID, "zip-code"))
    )
# на этой странице цвет задаётся не инлайн, а через класс,
# поэтому проводим проверку по классам alert-danger/alert-sucsses
    zip_classes = zip_error.get_attribute("class")
    assert "alert-danger" in zip_classes, (
        f"Ожидался класс alert-danger у #zip-code, получено: {zip_classes}"
    )

    success_ids = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]

    for field_id in success_ids:
        el = driver.find_element(By.ID, field_id)
        classes = el.get_attribute("class")
        assert "alert-success" in classes, (
            f"Ожидался класс alert-success у #{field_id}, получено: {classes}"
        )
