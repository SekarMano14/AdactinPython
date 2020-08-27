from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects import Locators


class ConformationPage():
    def __init__(self, driver):
        self.driver = driver

        self.orderNo = driver.find_element(By.ID, Locators.order_no_id)

    def getOrderNo(self):
        return self.orderNo
