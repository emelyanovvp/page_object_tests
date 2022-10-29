from .pages.login_page import LoginPage
from .pages.main_page import MainPage
def test_guest_should_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_url()
def test_guest_should_see_login_form(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_form()
def test_guest_should_see_register_form(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, url)
    page.open()
    page.should_be_register_form()
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
