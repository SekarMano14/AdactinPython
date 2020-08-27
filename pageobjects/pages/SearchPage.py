from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects import Locators


class SearchPage():
    def __init__(self, driver):
        self.driver = driver

        self.location = driver.find_element(By.ID, Locators.slt_location_id)
        self.hotel = driver.find_element(By.ID, Locators.slt_hotel_id)
        self.roomType = driver.find_element(By.ID, Locators.slt_roomtype_id)
        self.roomNo = driver.find_element(By.ID, Locators.slt_room_nos_id)
        self.dateIn = driver.find_element(By.ID, Locators.txt_date_in_id)
        self.dateOut = driver.find_element(By.ID, Locators.txt_date_out_id)
        self.adult = driver.find_element(By.ID, Locators.slt_adult_id)
        self.child = driver.find_element(By.ID, Locators.slt_child_id)
        self.btnSubmit = driver.find_element(By.ID, Locators.btn_submit_id)

    def getLocation(self):
        return self.location

    def getHotel(self):
        return self.hotel

    def getRoomType(self):
        return self.roomType

    def getRoomNo(self):
        return self.roomNo

    def getDateIn(self):
        return self.dateIn

    def getDateOut(self):
        return self.dateOut

    def getAdult(self):
        return self.adult

    def getChild(self):
        return self.child

    def getSubmit(self):
        return self.btnSubmit
