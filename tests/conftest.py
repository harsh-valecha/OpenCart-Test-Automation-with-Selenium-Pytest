import pytest
from selenium import webdriver
from utils.driver_factory import get_driver


def driver():
    driver = get_driver()
    yield driver
    driver.quit()