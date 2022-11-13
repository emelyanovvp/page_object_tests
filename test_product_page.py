import time
import pytest
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException
@pytest.mark.need_review
class TestUserAddToBasketFromProductPage() :
    @pytest.fixture()
    def setup(self):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser,link)
        page.open()
        page.register_new_user_and_go_to_main_page()
        main_page = BasePage(browser, browser.current_url)
        main_page.open()
        main_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = BasePage(browser, link)
        page.open()
        page.should_not_be_success_message()
    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = BasePage(browser, link)
        page.open()
        page.guest_can_add_product_to_basket()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.open()
    basket_page.should_be_text_that_basket_is_empty()
    basket_page.should_not_be_product_in_basket()
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasePage(browser, link)
    page.open()
    page.guest_can_go_to_catalog()
    catalog_page = BasePage(browser, browser.current_url)
    catalog_page.open()
    catalog_page.guest_can_add_product_to_basket()

def test_user_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.open()
    login_page.register_new_user_and_go_to_main_page()
    main_page = BasePage(browser,browser.current_url)
    main_page.open()
    main_page.should_be_authorized_user()
    main_page.guest_can_go_to_catalog()
    catalog_page = BasePage(browser, browser.current_url)
    catalog_page.open()
    catalog_page.guest_can_add_product_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    page = ProductPage(browser, link)
    page.open()
    page.push_button_add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    page = ProductPage(browser, link)
    page.open()
    page.push_button_add_to_basket()
    time.sleep(1)
    page.is_disappeared_after_adding_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()




if __name__ == '__main__':
    pytest.main()
