import time

from Pages.home_page import HomePage

from utilities.config_reader import read_config

from utilities.csv_reader import read_test_data

from utilities.screenshot import take_screenshot


def test_search_product(driver):

    try:

        # Read configuration
        config = read_config()
        time.sleep(2)

        # Read product from CSV
        data = read_test_data("test_data/test_data.csv")
        product_name = data[0]["product"]
        time.sleep(2)

        # Open website
        driver.get(config["url"])
        time.sleep(3)

        # Search product
        home_page = HomePage(driver)
        home_page.search_product(product_name)
        time.sleep(3)

        # Verify product
        assert home_page.is_product_displayed(product_name)
        time.sleep(3)

    except Exception:

        take_screenshot(driver, "search_failed")

        raise