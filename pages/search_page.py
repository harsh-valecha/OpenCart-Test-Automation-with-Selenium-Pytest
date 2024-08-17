import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from opencart_automation.utils.config import Config


class SearchPage:
    def __init__(self,driver:WebDriver):
        self.driver:WebDriver = driver
        self.driver.get(Config.SEARCH_URL)
        self.page_title = (By.TAG_NAME,'h1')
        self.keywords_txt = (By.XPATH,"//input[contains(@placeholder,'Keywords')]")
        self.categories_select = (By.XPATH,"//select[@name='category_id']")
        self.subcategories_check = (By.XPATH,"//input[@name='sub_category']")
        self.description_check = (By.XPATH,"//input[@id='description']")
        self.search_btn = (By.XPATH,"//input[@value='Search']")

    def check_search_page(self)->bool:
        # validates if the page is search page
        if self.driver.find_element(*self.page_title).is_displayed():
            return True

        else:
            return False


    def type_keywords(self,value:list[str]) -> None:
        # if a keyword is single i will type keyword and click enter
        keyword_element = self.driver.find_element(*self.keywords_txt)
        if len(value)<=1:
            keyword_element.send_keys(*value)
            keyword_element.send_keys(Keys.ENTER)
        else:
            keyword_element.send_keys(*value)






