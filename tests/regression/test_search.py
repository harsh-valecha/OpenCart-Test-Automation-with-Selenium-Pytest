import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from opencart_automation.pages.search_page import SearchPage
from opencart_automation.pages.login_page import LoginPage


# this test_login will be required later when we have to first login and then perform action
@pytest.mark.skip
def test_login(driver:WebDriver):
    page = LoginPage(driver)
    page.type_email('dnewiss0@usatoday.com')
    page.type_password('bR4Dv)>>GS6rqayT')
    page.click_login()
    assert driver.current_url.endswith('?route=account/account')
    print(f'user is logged in successfully')
    return driver



def test_search_one_keyword(driver:WebDriver):
    #driver:WebDriver = test_login(driver)
    page = SearchPage(driver)
    page.type_keywords_and_enter('iphone')
    page.product_name_check('iphone')
    print('product search working correctly')
