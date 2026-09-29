from typing import TYPE_CHECKING
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Для избежания циклического импорта при типизации
if TYPE_CHECKING:
    from pages.checkout_page import CheckoutPage


class CartPage:
    """
    Класс страницы корзины покупок.

    Предоставляет методы для взаимодействия с элементами
    страницы корзины и перехода к оформлению заказа.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        :param driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы элементов страницы
        self.CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button#checkout")

    def go_to_checkout(self) -> "CheckoutPage":
        """
        Переходит к оформлению заказа, нажимая кнопку Checkout.

        :return: Экземпляр CheckoutPage для продолжения цепочки действий
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
        return self
