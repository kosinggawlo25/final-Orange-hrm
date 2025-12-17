import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from helpers import login, open_recruitment


def test_login(driver):
    driver, wait = driver
    login(driver, wait)
    assert "dashboard" in driver.current_url


def test_open_recruitment(driver):
    driver, wait = driver
    login(driver, wait)
    open_recruitment(driver, wait)
    assert "recruitment" in driver.current_url


def test_add_candidate(driver):
    driver, wait = driver
    login(driver, wait)
    open_recruitment(driver, wait)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[.=' Add ']"))
    ).click()
    time.sleep(2)

    wait.until(EC.visibility_of_element_located((By.NAME, "firstName"))).send_keys("Joshua")
    wait.until(EC.visibility_of_element_located((By.NAME, "middleName"))).send_keys("Vestil")
    driver.find_element(By.NAME, "lastName").send_keys("Arcilla")

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//label[text()='Vacancy']/following::div[1]"))
    ).click()

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='Junior Account Assistant']"))
    ).click()

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//label[text()='Email']/following::input[1]"))
    ).send_keys("Joshua@gmail.com")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    assert "addCandidate" in driver.current_url


def test_search_candidate_by_name(driver):
    driver, wait = driver
    login(driver, wait)
    open_recruitment(driver, wait)

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Type for hints...']"))
    ).send_keys("Joshua")

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='listbox']//span"))
    ).click()

    driver.find_element(By.XPATH, "//button[.=' Search ']").click()
    time.sleep(3)

    assert True


def test_reset_filters(driver):
    driver, wait = driver
    login(driver, wait)
    open_recruitment(driver, wait)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[.=' Reset ']"))
    ).click()

    assert True


def test_view_candidate(driver):
    driver, wait = driver
    login(driver, wait)
    open_recruitment(driver, wait)

    driver.find_element(By.XPATH, "//button[.=' Search ']").click()

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//i[contains(@class,'bi-eye')]"))
    ).click()

    assert True


def test_delete_candidate(driver):
    driver, wait = driver
    login(driver, wait)
    open_recruitment(driver, wait)

    driver.find_element(By.XPATH, "//button[.=' Search ']").click()
    time.sleep(2)

    driver.find_element(
        By.XPATH, "//button[contains(@class,'oxd-icon-button')][2]"
    ).click()
    time.sleep(2)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[.=' Yes, Delete ']")
    )).click()
    time.sleep(3)

    assert True