from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
class ProductPage(BasePage):
    def push_button_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()
    def check_names_of_product(self):
        product_to_choose_element = self.browser.find_element(*ProductPageLocators.GETTING_NAME)
        product_to_choose = product_to_choose_element.text
        message_product_added_to_basket_element = self.browser.find_element(*ProductPageLocators.GETTING_MESSAGE_NAME)
        message_product_added_to_basket = message_product_added_to_basket_element.text
        assert product_to_choose == message_product_added_to_basket, "Product is not in basket"
    def check_prices_of_product(self):
        price_of_product_element = self.browser.find_element(*ProductPageLocators.GETTING_PRICE)
        price_of_product = price_of_product_element.text
        message_how_much_is_basket_total_element = self.browser.find_element(*ProductPageLocators.GETTING_MESSAGE_PRICE)
        message_how_much_is_basket_total = message_how_much_is_basket_total_element.text
        assert price_of_product == message_how_much_is_basket_total, "Price of product is not equal basket total"
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.GETTING_MESSAGE_NAME), \
            "Success message is presented, but should not be"
    def is_disappeared_after_adding_product_to_basket(self):
        assert  self.is_disappeared(*ProductPageLocators.GETTING_MESSAGE_NAME), \
            "Success message is presented, but should not be"
    def guest_should_see_login_link_on_product_page(self):
        assert  self.should_be_login_link(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
    def guest_can_go_to_login_page_from_product_page(self):
        assert  self.go_to_login_page(*BasePageLocators.LOGIN_LINK), "Can't go login page"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), "Product is presented, but should not be"

    def should_be_text_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_IS_EMPTY), "No text that basket is empty"
