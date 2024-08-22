import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from opencart_automation.pages.search_page import SearchPage
from opencart_automation.tests.conftest import login
import time

def test_add_to_cart_from_search(driver:WebDriver):
    driver = login(driver)
    page = SearchPage(driver)
    page.type_keywords_and_enter('apple')
    page.click_add_to_cart()
    # driver.execute_script("arguments[0].style.display='block';", btn)
    # btn.click()
    # driver.execute_script("arguments[0].click();",btn)
    time.sleep(2)
    assert driver.current_url =='https://awesomeqa.com/ui/index.php?route=product/product&product_id=42'

