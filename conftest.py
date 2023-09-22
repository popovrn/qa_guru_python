import pytest
from selene import  browser
from selene.support.shared import browser


@pytest.fixture()
def browser_setings():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    browser.open('https://google.com')






