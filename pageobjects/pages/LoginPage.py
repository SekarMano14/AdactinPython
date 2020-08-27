from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects import Locators


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.userName = driver.find_element(By.ID, Locators.txt_userName_id)
        self.password = driver.find_element(By.ID, Locators.txt_password_id)
        self.btnLogin = driver.find_element(By.ID, Locators.btn_login_id)

    def getUserName(self):
        return self.userName

    def getPassword(self):
        return self.password

    def getLogin(self):
        return self.btnLogin
