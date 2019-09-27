import pytest
from selenium import webdriver

@pytest.yield_fixture(scope='session')
def invoke(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', False)
    _driver = webdriver.Chrome(options=options)

    return _driver

# @pytest.fixture(scope='session', autouse=True)
# def close(request, driver):
#     def fin():
#         driver.quit()
#     request.addfinalizer()