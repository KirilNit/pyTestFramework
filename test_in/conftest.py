import pytest
from driver import WebDriver
from selenium import webdriver

@pytest.yield_fixture(scope='session')
def invoke(request):
    """invoke"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', False)
    _driver = webdriver.Chrome(options=options)

    return _driver

@pytest.mark.usefixtures('invoke')
def loging_page(request):
    """new comment"""
    pass

