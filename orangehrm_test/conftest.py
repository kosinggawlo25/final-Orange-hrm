import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(2)

    yield driver, wait

    time.sleep(2)
    driver.quit()
