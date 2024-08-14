import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.config import Config

class HomePage:
    def __init__(self,driver:WebDriver):
        self.driver:WebDriver = driver
        self.driver.get(Config.BASE_URL)
        self.search_txt = (By.NAME,"search")
        self.search_btn = (By.XPATH,"//i[@class='fa fa-search']")
        self.products_cards = (By.CLASS_NAME,"product-thumb")

    def type_search(self,value):
        self.driver.find_element(*self.search_txt).send_keys(value)

    def click_search(self):
        self.driver.find_element(*self.search_btn).click()


    def get_products_title(self)->list[str]:
        products = self.driver.find_elements(*self.products_cards)
        product_title = []
        for product in products:
            product_title.append(product.find_element(By.XPATH,"//div/h4/a").text)
        return product_title


