import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from opencart_automation.utils.config import Config
from opencart_automation.pages.home_page import HomePage


@pytest.mark.dependency(depends=["login"])
def test_wishlist(driver:WebDriver):
    home = HomePage(driver)
    home.type_search('iphone')
    home.click_search()
    ## add product to wishlist

