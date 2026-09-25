import pytest
from selenium import webdriver

from utilities.config_reader import read_config


@pytest.fixture
def driver():

    config = read_config()

    if config["browser"].lower() == "chrome":
        driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    driver.quit()