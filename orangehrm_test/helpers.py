import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def login(driver, wait):
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
    time.sleep(1)

    driver.find_element(By.NAME, "password").send_keys("admin123")
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)


def open_recruitment(driver, wait):
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Recruitment']")
        )
    ).click()
    time.sleep(3)
