from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Класс страницы оформления заказа.

    Предоставляет методы для заполнения формы доставки,
    перехода к следующему этапу и получения информации о заказе.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.

        :param driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы элементов страницы
        self.FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input#first-name")
        self.LAST_NAME_INPUT = (By.CSS_SELECTOR, "input#last-name")
        self.POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "input#postal-code")
        self.CONTINUE_BUTTON = (By.CSS_SELECTOR, "input#continue")
        self.TOTAL_LABEL = (By.CSS_SELECTOR, "div.summary_total_label")

    def fill_checkout_form(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> "CheckoutPage":
        """
        Заполняет форму оформления заказа и переходит к следующему этапу.

        :param first_name: Имя покупателя
        :param last_name: Фамилия покупателя
        :param postal_code: Почтовый индекс для доставки
        :return: Экземпляр CheckoutPage для продолжения цепочки вызовов
        """
        # Заполнение поля имени
        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME_INPUT)
        ).send_keys(first_name)

        # Заполнение поля фамилии
        self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME_INPUT)
        ).send_keys(last_name)

        # Заполнение поля почтового индекса
        self.wait.until(
            EC.visibility_of_element_located(self.POSTAL_CODE_INPUT)
        ).send_keys(postal_code)

        # Нажатие кнопки продолжения
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

        return self

    def get_total_text(self) -> str:
        """
        Получает текст итоговой суммы заказа.

        :return: Текст элемента с общей суммой (например, "Total: $XX.XX")
        """
        total = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        )
        return total.text.strip()
