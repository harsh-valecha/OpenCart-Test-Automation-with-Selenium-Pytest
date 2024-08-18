import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from opencart_automation.pages.search_page import SearchPage
from opencart_automation.pages.login_page import LoginPage


@pytest.mark.dependency(name='login')
def test_login(driver:WebDriver):
    page = LoginPage(driver)
    page.type_email('dnewiss0@usatoday.com')
    page.type_password('bR4Dv)>>GS6rqayT')
    page.click_login()
    assert driver.current_url.endswith('?route=account/account')
    print(f'user is logged in successfully')




@pytest.mark.dependency(depends=['login'])
def test_search_one_keyword(driver:WebDriver):
    page = SearchPage(driver)
    page.type_keywords("iphone")

