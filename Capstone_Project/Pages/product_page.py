from selenium.webdriver.common.by import By


class ProductPage:

    ADD_TO_CART_BUTTON = (
        By.ID,
        "button-cart"
    )

    SHOPPING_CART = (
        By.CSS_SELECTOR,
        "a[title='Shopping Cart']"
    )

    def __init__(self, driver):
        self.driver = driver

    def click_add_to_cart(self):
        self.driver.find_element(
            *self.ADD_TO_CART_BUTTON
        ).click()

    def go_to_cart(self):
        self.driver.find_element(
            *self.SHOPPING_CART
        ).click()