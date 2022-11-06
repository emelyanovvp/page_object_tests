from selenium.webdriver.common.by import By
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a.btn-default")
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    GETTING_NAME = (By.CSS_SELECTOR,"div.product_main h1")
    GETTING_PRICE = (By.CSS_SELECTOR,"div.product_main p")
    GETTING_MESSAGE_NAME = (By.CSS_SELECTOR, "#messages .alertinner > strong")
    GETTING_MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner > p > strong")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a")
class BasketPageLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR,".row > h2.h3")
    TEXT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")


