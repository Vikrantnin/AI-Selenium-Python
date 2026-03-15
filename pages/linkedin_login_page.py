from selenium.webdriver.common.by import By

class LinkedInLoginPage:

    def __init__(self, driver):  #constructor
        self.driver = driver

    username = (By.ID, "username")
    password = (By.ID, "password")
    sign_in = (By.XPATH, "//button[@type='submit']")

    def login(self, user, pwd):

        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.sign_in).click()