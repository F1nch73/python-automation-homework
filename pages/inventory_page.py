from typing import TYPE_CHECKING
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Для избежания циклического импорта при типизации
if TYPE_CHECKING:
    from pages.cart_page import CartPage


class InventoryPage:
    """
    Класс страницы каталога товаров.

    Предоставляет методы для добавления товаров в корзину
    и перехода на страницу корзины покупок.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы каталога товаров.

        :param driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Кнопки «Add to cart» для товаров
        self.BACKPACK_ADD_BTN = (
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        self.TSHIRT_ADD_BTN = (
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        self.ONESIE_ADD_BTN = (
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")

        # Иконка корзины
        self.CART_LINK = (By.CSS_SELECTOR, "a.shopping_cart_link")

    def add_backpack(self) -> "InventoryPage":
        """
        Добавляет товар «Sauce Labs Backpack» в корзину.

        :return: Экземпляр InventoryPage для продолжения цепочки вызовов
        """
        self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK_ADD_BTN)
        ).click()
        return self

    def add_tshirt(self) -> "InventoryPage":
        """
        Добавляет товар «Sauce Labs Bolt T-Shirt» в корзину.

        :return: Экземпляр InventoryPage для продолжения цепочки вызовов
        """
        self.wait.until(
            EC.element_to_be_clickable(self.TSHIRT_ADD_BTN)
        ).click()
        return self

    def add_onesie(self) -> "InventoryPage":
        """
        Добавляет товар «Sauce Labs Onesie» в корзину.

        :return: Экземпляр InventoryPage для продолжения цепочки вызовов
        """
        self.wait.until(
            EC.element_to_be_clickable(self.ONESIE_ADD_BTN)
        ).click()
        return self

    def go_to_cart(self) -> "CartPage":
        """
        Переходит на страницу корзины покупок.

        :return: Экземпляр CartPage для продолжения цепочки действий
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)
