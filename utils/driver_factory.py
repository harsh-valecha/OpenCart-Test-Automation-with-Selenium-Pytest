from selenium import webdriver
from config import Config

def get_driver():
    if Config.BROWSER=='chrome':
        return webdriver.Chrome()
    if Config.BROWSER=='firefox':
        return webdriver.Firefox()
    else:
        return f"{Config.BROWSER} is not supported"
