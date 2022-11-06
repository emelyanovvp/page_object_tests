from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT),"Product is presented, but should not be"

    def should_be_text_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_IS_EMPTY), "No text that basket is empty"

