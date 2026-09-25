import time

from Pages.home_page import HomePage

from Pages.product_page import ProductPage

from Pages.cart_page import CartPage

from utilities.csv_reader import read_test_data

from utilities.screenshot import take_screenshot
from utilities.config_reader import read_config


def test_add_product_to_cart(driver):

    try:

        # Read configuration
        config = read_config()
        time.sleep(2)


        # 1. Open website
        driver.get(config["url"])
        time.sleep(3)

        # 2. Read product name from CSV
        data = read_test_data("test_data/test_data.csv")
        product_name = data[0]["product"]
        time.sleep(2)

        # 3. Search product
        home_page = HomePage(driver)
        home_page.search_product(product_name)
        time.sleep(3)

        # 4. Verify product is displayed
        assert home_page.is_product_displayed(product_name)
        time.sleep(2)

        # 5. Click product
        driver.find_element(
            "link text",
            product_name
        ).click()
        time.sleep(3)

        # 6. Add product to cart
        product_page = ProductPage(driver)
        product_page.click_add_to_cart()
        time.sleep(3)

        # 7. Go to shopping cart
        product_page.go_to_cart()
        time.sleep(3)

        # 8. Verify product is in cart
        cart_page = CartPage(driver)
        assert cart_page.is_product_in_cart(product_name)
        time.sleep(3)

        print("PASS: Product is successfully added to cart")

    except Exception:

        take_screenshot(driver, "cart_failed")

        raise