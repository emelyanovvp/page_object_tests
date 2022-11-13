from .base_page import BasePage
from .locators import LoginPageLocators

from selenium.webdriver.common.by import By
import time
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    def should_be_login_url(self):
        assert "login" in self.browser.current_url , "Login url is not presented"
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
    def register_new_user_and_go_to_main_page(self):
        email_address = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email = str(time.time()) + "@fakemail.org"
        email_address.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password1.send_keys("161257123")
        password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2.send_keys("161257123")
        registration_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        registration_submit.click()
        main_page = BasePage(self.browser, self.browser.current_url)
        main_page.open()


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.GETTING_MESSAGE_NAME), \
            "Success message is presented, but should not be"


