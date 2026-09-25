from selenium.webdriver.common.by import By


class LoginPage: #this class represents the login page.

    # Locators
    EMAIL = (By.ID, "input-email") #stores location of email box
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):  #give  me  an email and i will type into the email box
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()