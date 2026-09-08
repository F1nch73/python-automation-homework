import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless")  # при необходимости
    drv = webdriver.Firefox(options=options)
    drv.implicitly_wait(10)
    yield drv
    drv.quit()


def test_saucedemo_checkout(driver):
    url = "https://www.saucedemo.com/"

    # 1. Авторизация
    login_page = LoginPage(driver).open(url)
    login_page.login("standard_user", "secret_sauce")

    # 2. Добавление товаров в корзину
    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack().add_tshirt().add_onesie()

    # 3. Переход в корзину
    inventory_page.go_to_cart()

    # 4. Переход к оформлению
    cart_page = CartPage(driver)
    cart_page.go_to_checkout()

    # 5. Заполнение формы
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form(
        first_name="Nikita",
        last_name="Pidunov",
        postal_code="400000"
    )

    # 6. Проверка итоговой суммы
    total_text = checkout_page.get_total_text()
    expected_total = "$58.29"

    assert expected_total in total_text, (
        f"Итоговая сумма должна быть {expected_total}, "
        f"получено: {total_text}"
    )
