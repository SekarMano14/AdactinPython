import pytest
import pytest_html
from base.Base import BaseClass
from pageobjects.pages.LoginPage import LoginPage
from pageobjects.pages.SearchPage import SearchPage
from pageobjects.pages.SelectPage import SelectPage
from pageobjects.pages.BookingPage import BookingPage
from pageobjects.pages.ConformationPage import ConformationPage


class TestAdactinBooking():
    def test_adactin(self):
            b = BaseClass()
            driver = b.launch_Browser()
            b.load_Url("http://adactinhotelapp.com/index.php")
            driver.implicitly_wait(25)
            b.maxmize_window()
            # login
            l = LoginPage(driver)
            b.type(l.getUserName(), "mkck4695")
            b.type(l.getPassword(), "mkck4695")
            b.btn_click(l.getLogin())

            # search
            s = SearchPage(driver)
            b.select_by_value(s.getLocation(), "Sydney")
            b.select_by_value(s.getHotel(), "Hotel Sunshine")
            b.select_by_value(s.getRoomType(), "Standard")
            b.select_by_value(s.getRoomNo(), "1")
            b.type(s.getDateIn(), "13/08/2020")
            b.type(s.getDateOut(), "13/08/2020")
            b.select_by_value(s.getAdult(), "2")
            b.select_by_value(s.getChild(), "2")
            b.btn_click(s.getSubmit())

            # selecHotel
            se = SelectPage(driver)
            b.btn_click(se.getSelectHotel())
            b.btn_click(se.getContinue())

            # BookHotel
            book = BookingPage(driver)
            b.type(book.getFirstName(), "Manoj")
            b.type(book.getLasttName(), "Sekar")
            b.type(book.getAddress(), "Namakkal")
            b.type(book.getCardNo(), "6235987456321457")
            b.select_by_value(book.getCardType(), "VISA")
            b.select_by_text(book.getExpireMonth(), "August")
            b.select_by_text(book.getExpireYear(), "2022")
            b.type(book.getCcvNo(), "456")
            b.btn_click(book.getBookinBtn())

            # Conformation
            c = ConformationPage(driver)
            orderNo = b.get_attribute(c.getOrderNo())
            print(orderNo)

            b.quit_browser()
