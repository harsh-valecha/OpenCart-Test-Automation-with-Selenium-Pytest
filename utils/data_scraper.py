from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

def get_data_from_element(driver:WebDriver,url:str,web_element:tuple)->list:
    driver.get(url)
    elements = driver.find_elements(*web_element)
    data = []
    for element in elements:
        data.append(element.text)
    return data



# for unit testing
# url = 'https://awesomeqa.com/ui/index.php?route=product/category&path=20'
# product_name = (By.XPATH,"//div[@class='caption']/h4/a")
# product_price = (By.XPATH,"//p[@class='price']")
# names = get_data_from_element(driver=webdriver.Chrome(),url=url,web_element=product_name)
# price= get_data_from_element(driver=webdriver.Chrome(),url=url,web_element=product_price)
# print(names)
# name_ = ['Apple Cinema 30"', 'Canon EOS 5D', 'HP LP3065', 'HTC Touch HD', 'iPhone', 'iPod Classic', 'MacBook', 'MacBook Air', 'Palm Treo Pro', 'Product 8', 'Samsung SyncMaster 941BW', 'Sony VAIO']
# price_ = ['$110.00 $122.00\nEx Tax: $90.00', '$98.00 $122.00\nEx Tax: $80.00', '$122.00\nEx Tax: $100.00', '$122.00\nEx Tax: $100.00', '$123.20\nEx Tax: $101.00', '$122.00\nEx Tax: $100.00', '$602.00\nEx Tax: $500.00', '$1,202.00\nEx Tax: $1,000.00', '$337.99\nEx Tax: $279.99', '$122.00\nEx Tax: $100.00', '$242.00\nEx Tax: $200.00', '$1,202.00\nEx Tax: $1,000.00']
# print(price)