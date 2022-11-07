import time
import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException

@pytest.mark.important
class TestUserAddToBasketFromProductPage() :
    @pytest.fixture(scope="function")
    def setup_login(self):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser,link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()
    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.push_button_add_to_basket()
        page.check_names_of_product()
        page.check_prices_of_product()

#@pytest.mark.xfail
#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    #page = ProductPage(browser, link)
    #page.open()
    #page.push_button_add_to_basket()
    #page.should_not_be_success_message()


#@pytest.mark.xfail
#def test_message_disappeared_after_adding_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    #page = ProductPage(browser, link)
    #page.open()
    #page.push_button_add_to_basket()
    #time.sleep(1)
    #page.is_disappeared_after_adding_product_to_basket()
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

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_text_that_basket_is_empty()
    basket_page.should_not_be_product_in_basket()


if __name__ == '__main__':
    pytest.main()
