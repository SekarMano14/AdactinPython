from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects import Locators


class SelectPage():
    def __init__(self, driver):
        self.driver = driver

        self.selectHotel = driver.find_element(By.ID, Locators.select_hotel_id)
        self.btn_continue = driver.find_element(By.ID, Locators.btn_continue_id)

    def getSelectHotel(self):
        return self.selectHotel

    def getContinue(self):
        return self.btn_continue
