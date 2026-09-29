"""
Тестовые сценарии для интернет-магазина Sauce Demo.

Модуль содержит тесты проверки полного цикла покупки:
от авторизации до оформления заказа и проверки итоговой суммы.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Generator

import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    """
    Фикстура для создания и настройки WebDriver экземпляра.

    Создаёт браузер Firefox, настраивает неявное ожидание
    и автоматически закрывает браузер после завершения теста.

    :return: WebDriver экземпляр для управления браузером
    """
    options = Options()
    # options.add_argument("--headless")  # при необходимости
    drv = webdriver.Firefox(options=options)
    drv.implicitly_wait(10)
    yield drv
    drv.quit()


@allure.feature("Оформление заказа")
@allure.story("Полный цикл покупки")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Покупка трёх товаров с проверкой итоговой суммы")
@allure.description(
    "Тест проверяет полный цикл покупки: авторизация, добавление трёх товаров "
    "(Backpack, T-Shirt, Onesie) в корзину, переход к оформлению, заполнение "
    "формы доставки и проверка корректности итоговой суммы заказа"
)
@allure.tag("checkout", "smoke", "e2e")
@allure.id("test_saucedemo_checkout_001")
def test_saucedemo_checkout(driver: WebDriver) -> None:
    """
    Тест полного цикла покупки в Sauce Demo.

    Проверяет:
    - Успешную авторизацию
    - Добавление товаров в корзину
    - Переход к оформлению заказа
    - Заполнение формы доставки
    - Корректность расчёта итоговой суммы
    """
    url = "https://www.saucedemo.com/"

    # Шаг 1: Авторизация
    with allure.step("Авторизоваться под пользователем 'standard_user'"):
        login_page = LoginPage(driver).open(url)
        login_page.login("standard_user", "secret_sauce")

    # Шаг 2: Добавление товаров в корзину
    with allure.step("Добавить Sauce Labs Backpack в корзину"):
        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack()

    with allure.step("Добавить Sauce Labs Bolt T-Shirt в корзину"):
        inventory_page.add_tshirt()

    with allure.step("Добавить Sauce Labs Onesie в корзину"):
        inventory_page.add_onesie()

    # Шаг 3: Переход в корзину
    with allure.step("Перейти на страницу корзины"):
        inventory_page.go_to_cart()

    # Шаг 4: Переход к оформлению
    with allure.step("Перейти к оформлению заказа"):
        cart_page = CartPage(driver)
        cart_page.go_to_checkout()

    # Шаг 5: Заполнение формы доставки
    with allure.step(
        "Заполнить форму: имя 'Nikita', фамилия 'Pidunov', индекс '400000'"
    ):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_form(
            first_name="Nikita",
            last_name="Pidunov",
            postal_code="400000"
        )

    # Шаг 6: Проверка итоговой суммы
    with allure.step("Проверить итоговую сумму заказа '$58.29'"):
        total_text = checkout_page.get_total_text()
        expected_total = "$58.29"

        assert expected_total in total_text, (
            f"Итоговая сумма должна быть {expected_total}, "
            f"получено: {total_text}"
        )
