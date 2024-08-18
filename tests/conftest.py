import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from opencart_automation.utils.driver_factory import get_driver
from opencart_automation.utils.config import Config
from opencart_automation.pages.login_page import LoginPage


@pytest.fixture(scope='function')
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


