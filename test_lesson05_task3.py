from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    links = driver.find_elements(By.CSS_SELECTOR, "a[href]")

    assert len(links) == 9, f"Ожидалось 9 ссылок, найдено: {len(links)}"

    for i, link in enumerate(links):
        assert link.is_displayed(), f"Ссылка #{i} не отображается"

    first_link_text = links[0].text
    assert "1" in first_link_text, (
        f"Текст первой ссылки не содержит '1'. Текст: '{first_link_text}'"
    )

    driver.quit()
