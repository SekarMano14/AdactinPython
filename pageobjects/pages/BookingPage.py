from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects import Locators


class BookingPage():
    def __init__(self, driver):
        self.driver = driver

        self.firstName = driver.find_element(By.ID, Locators.txt_firstname_id)
        self.lastName = driver.find_element(By.ID, Locators.txt_lastname_id)
        self.address = driver.find_element(By.ID, Locators.txt_address_id)
        self.cardNo = driver.find_element(By.ID, Locators.txt_cardno_id)
        self.cardType = driver.find_element(By.ID, Locators.slt_cardtype_id)
        self.expireMonth = driver.find_element(By.ID, Locators.slt_expmnth_id)
        self.expireYear = driver.find_element(By.ID, Locators.slt_expyear_id)
        self.ccvNo = driver.find_element(By.ID, Locators.txt_ccv_id)
        self.btnBook = driver.find_element(By.ID, Locators.btn_book_id)

    def getFirstName(self):
        return self.firstName

    def getLasttName(self):
        return self.lastName

    def getAddress(self):
        return self.address

    def getCardNo(self):
        return self.cardNo

    def getCardType(self):
        return self.cardType

    def getExpireMonth(self):
        return self.expireMonth

    def getExpireYear(self):
        return self.expireYear

    def getCcvNo(self):
        return self.ccvNo

    def getBookinBtn(self):
        return self.btnBook
