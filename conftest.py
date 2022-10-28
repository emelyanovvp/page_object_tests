from selenium import webdriver

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en or ru")