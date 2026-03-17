import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new") #Run browser without GUI
    options.add_argument("--no-sandbox") #Required for CI containers
    options.add_argument("--disable-dev-shm-usage") #Prevent memory crash
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    driver.set_page_load_timeout(50)

    yield driver

    driver.quit()


# Screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            # Ensure folder exists
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"screenshots/{item.name}_{timestamp}.png"

            driver.save_screenshot(file_name)
            print(f"\nScreenshot saved: {file_name}")