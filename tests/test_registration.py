import pytest
from pages.registration_page import RegistrationPage
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.mark.smoke
# @pytest.mark.parametrize
def test_registration(driver:WebDriver):
    page = RegistrationPage(driver)
    page.type_firstname("Kamlish")
    page.type_lastname("Chattu")
    page.type_email("kamleschattu@gmail.com")
    page.type_telephone("98567890")
    page.type_password("ok123")
    page.type_confirm_password("ok123")
    page.click_no_subscribe()
    page.click_agree()
    page.click_continue()
    # checks for user warning regarding user already exist
    assert page.check_warning_exist()
    # checks if url ends with success pattern
    assert driver.current_url.endswith('account/success')

