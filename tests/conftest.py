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


def login(driver:WebDriver):
    page = LoginPage(driver)
    page.type_email('dnewiss0@usatoday.com')
    page.type_password('bR4Dv)>>GS6rqayT')
    page.click_login()
    return driver
