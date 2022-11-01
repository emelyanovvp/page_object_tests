from selenium.common.exceptions import NoAlertPresentException
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.push_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_names_of_product()
    page.check_prices_of_product()

