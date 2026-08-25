from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()

    try:
        # --- Пользователь 1 ---
        driver.get("https://gitflic.ru/")

        # Добавляем cookie сессии
        driver.add_cookie({
            "name": "SESSION",
            "value": "NTllMWFiNGItNjlhYS00NGFiLThlZGMtYzgzN2U3NGUxOTk5",
            "domain": "gitflic.ru",
        })

        driver.add_cookie({
            "name": "cookiesAccepted",
            "value": "true",
            "domain": "gitflic.ru",
        })

        driver.refresh()

        driver.get("https://gitflic.ru/user/definitlynotatestUser1")
        url_user1 = driver.current_url
        print(f"URL пользователя 1: {url_user1}")

        # --- Разлогиниваемся ---
        driver.delete_all_cookies()
        driver.get("https://gitflic.ru/")

        # --- Пользователь 2 ---
        driver.add_cookie({
            "name": "SESSION",
            "value": "MDk0MjdhYzItYjFiYy00NmMxLWJmNzItOTI5OTA1YWY0MmVi",
            "domain": "gitflic.ru",
        })

        driver.add_cookie({
            "name": "cookiesAccepted",
            "value": "true",
            "domain": "gitflic.ru",
        })

        driver.refresh()

        driver.get("https://gitflic.ru/user/definitlynotatestUser2")
        url_user2 = driver.current_url
        print(f"URL пользователя 2: {url_user2}")

        # Проверка
        assert url_user1 != url_user2, (
            f"URL пользователей совпадают!\n"
            f"User1: {url_user1}\n"
            f"User2: {url_user2}"
        )
        print("Тест пройден!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_session_storage_auth()
