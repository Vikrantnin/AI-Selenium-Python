import pytest
from pages.linkedin_login_page import LinkedInLoginPage
from src.main import generate_login_data

@pytest.mark.parametrize("username, password", generate_login_data())
def test_linkedin_login(driver, username, password):

    driver.get("https://www.linkedin.com/login")

    login_page = LinkedInLoginPage(driver)

    login_page.login(username, password)