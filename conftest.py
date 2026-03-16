import pytest
from selenium import webdriver

@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver.implicitly_wait(5)
    driver.set_page_load_timeout(30)
    yield driver

    driver.quit()