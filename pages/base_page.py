from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import BasePageLocators
from .locators import MainPageLocators
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)
    def open(self):
        self.browser.get(self.url)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
    def go_to_product_page(self):
        link = self.browser.find_element(*BasePageLocators.ALL_PRODUCTS_LINK)
        link.click()
    def should_be_link_all_products(self):
        assert self.is_element_present(*MainPageLocators.LINK_ALL_PRODUCTS),"No link all_products"
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*MainPageLocators.BUTTON_ADD_TO_BASKET),"No button add_to_basket"

    def guest_can_go_to_catalog(self):
        assert self.is_element_present(*MainPageLocators.LINK_ALL_PRODUCTS), \
            "No link all_product or wrong locator"
        link_all_products = self.browser.find_element(*MainPageLocators.LINK_ALL_PRODUCTS)
        link_all_products.click()
    def guest_can_add_product_to_basket(self):
        assert self.is_element_present(*MainPageLocators.BUTTON_ADD_TO_BASKET), \
            "No button add_to_basket or wrong locator"
        button_add_to_basket = self.browser.find_element(*MainPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*MainPageLocators.GETTING_MESSAGE_NAME), \
            "Success message is presented, but should not be"


if __name__ == '__main__':
    pytest.main()
