from selene import browser
import pytest
from selenium import webdriver


@pytest.fixture(scope='function',autouse=True)
def browser_managment():
    browser.config.base_url = 'https://github.com'
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield

    browser.quit()
