from selenium import webdriver
from selenium.webdriver.support.select import Select

class BaseClass():
    def launch_Browser(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\ManoKutty\PycharmProjects\AdactinHotel\Driver\chromedriver.exe")
        return self.driver

    def load_Url(self, url):
        self.driver.get(url)

    def maxmize_window(self):
        self.driver.maximize_window()

    def type(self, element, value):
        element.send_keys(value)

    def btn_click(self, element):
        element.click()

    def get_attribute(self, element):
        attribute = element.get_attribute("value")
        return attribute

    def get_text(self, element):
        text = element.text
        return text

    def quit_browser(self):
        self.driver.quit()

    def select_by_index(self,element,index):
        s=Select(element)
        s.select_by_index(index)

    def select_by_value(self,element,value):
        s=Select(element)
        s.select_by_value(value)

    def select_by_text(self,element,text):
        s=Select(element)
        s.select_by_visible_text(text)