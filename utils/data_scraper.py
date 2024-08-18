from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

def get_data_from_element(driver:WebDriver,url:str,web_element:tuple)->list:
    driver.get(url)
    elements = driver.find_elements(*web_element)
    for element in elements:
        data = list(i.strip() for i in element.text.split('\n'))
    return data



# for unit testing
url = 'https://awesomeqa.com/ui/index.php?route=product/search'
element = (By.XPATH,"//select")
print(get_data_from_element(driver=webdriver.Chrome(),url=url,web_element=element))
