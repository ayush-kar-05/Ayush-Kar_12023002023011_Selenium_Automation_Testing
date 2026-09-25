from utilities.config_reader import read_config

import unittest
import time

from selenium import webdriver

from Pages.login_page import LoginPage

from selenium.webdriver.common.by import By

from utilities.csv_reader import read_test_data


class TestLogin(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        time.sleep(2)

    def test_login(self):

        config = read_config()
        time.sleep(2)

        data = read_test_data("test_data/test_data.csv")
        time.sleep(2)

        self.driver.get(config["url"])
        time.sleep(3)

        self.driver.find_element(
            By.XPATH,
            "//span[text()='My Account']"
        ).click()
        time.sleep(3)

        self.driver.find_element(
            By.LINK_TEXT,
            "Login"
        ).click()
        time.sleep(3)

        login_page = LoginPage(self.driver)

        login_page.enter_email(data[0]["email"])
        time.sleep(2)

        login_page.enter_password(data[0]["password"])
        time.sleep(2)

        login_page.click_login()
        time.sleep(4)

        self.assertIn(
            "My Account",
            self.driver.page_source
        )
        time.sleep(3)

    def tearDown(self):

        time.sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()