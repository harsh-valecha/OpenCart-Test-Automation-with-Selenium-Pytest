import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from utils.config import Config

@pytest.mark.dependency(depends=["login"])
def test_wishlist(driver:WebDriver):
    pass

