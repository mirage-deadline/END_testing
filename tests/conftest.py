import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    options.add_argument('chrome')
    options.add_argument('--start-in-incognito')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver: webdriver.Chrome = get_webdriver
    url = 'https://www.endclothing.com/ru'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
