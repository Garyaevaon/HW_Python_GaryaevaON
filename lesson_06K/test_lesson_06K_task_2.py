<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

def test_task2():
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    waits = browser.find_element(
        By.CSS_SELECTOR, "#delay")
    waits.clear()
    waits.send_keys("45")

    browser.find_element(
        By.XPATH, '//span[text()="7"]').click()
    browser.find_element(
        By.XPATH, '//span[text()="+"]').click()
    browser.find_element(
        By.XPATH, '//span[text()="8"]').click()
    browser.find_element(
        By.XPATH, '//span[text()="="]').click()

    waiter = WebDriverWait(browser, 50, 0.1)
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))

    assert "15" in browser.find_element(By.CSS_SELECTOR, "div.screen").text

    browser.quit()
=======
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

def test_task2():
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    waits = browser.find_element(
        By.CSS_SELECTOR, "#delay")
    waits.clear()
    waits.send_keys("45")

    browser.find_element(
        By.XPATH, '//span[text()="7"]').click()
    browser.find_element(
        By.XPATH, '//span[text()="+"]').click()
    browser.find_element(
        By.XPATH, '//span[text()="8"]').click()
    browser.find_element(
        By.XPATH, '//span[text()="="]').click()

    waiter = WebDriverWait(browser, 50, 0.1)
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))

    assert "15" in browser.find_element(By.CSS_SELECTOR, "div.screen").text

    browser.quit()
>>>>>>> a107a0e910ad774e2c10923a29bf6d8a467789b3
