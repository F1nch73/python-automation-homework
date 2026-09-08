from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
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

    def add_backpack(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK_ADD_BTN)
        ).click()
        return self

    def add_tshirt(self):
        self.wait.until(
            EC.element_to_be_clickable(self.TSHIRT_ADD_BTN)
        ).click()
        return self

    def add_onesie(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ONESIE_ADD_BTN)
        ).click()
        return self

    def go_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()
        return self
