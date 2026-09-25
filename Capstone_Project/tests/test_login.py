import time

from selenium.webdriver.common.by import By

from Pages.login_page import LoginPage

from utilities.config_reader import read_config

from utilities.csv_reader import read_test_data

from utilities.screenshot import take_screenshot


def test_login(driver):

    try:

        # Read configuration
        config = read_config()
        time.sleep(2)

        # Read test data from CSV
        data = read_test_data("test_data/test_data.csv")
        email = data[0]["email"]
        password = data[0]["password"]
        time.sleep(2)

        # Open URL from config.ini
        driver.get(config["url"])
        time.sleep(3)

        # My Account
        driver.find_element(
            By.XPATH,
            "//span[text()='My Account']"
        ).click()
        time.sleep(3)

        # Login
        driver.find_element(
            By.LINK_TEXT,
            "Login"
        ).click()
        time.sleep(3)

        # Login using POM
        login_page = LoginPage(driver)
        login_page.enter_email(email)
        time.sleep(2)

        login_page.enter_password(password)
        time.sleep(2)

        login_page.click_login()
        time.sleep(4)

        # Verification
        assert "My Account" in driver.page_source
        time.sleep(3)

    except Exception:

        take_screenshot(driver, "login_failed")

        raise