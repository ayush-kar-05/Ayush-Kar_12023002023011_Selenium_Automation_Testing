from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def is_product_in_cart(self, product_name):
        product = self.driver.find_element(
            By.LINK_TEXT,
            product_name
        )
        return product.is_displayed()