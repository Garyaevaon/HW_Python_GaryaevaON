from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage_calculator:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def enter_value(self, trem):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(trem)

    def press_button_0(self):
        self._driver.find_element(By.XPATH, '//span[text()="0"]').click()

    def press_button_1(self):
        self._driver.find_element(By.XPATH, '//span[text()="1"]').click()

    def press_button_2(self):
        self._driver.find_element(By.XPATH, '//span[text()="2"]').click()

    def press_button_3(self):
        self._driver.find_element(By.XPATH, '//span[text()="3"]').click()

    def press_button_4(self):
        self._driver.find_element(By.XPATH, '//span[text()="4"]').click()

    def press_button_5(self):
        self._driver.find_element(By.XPATH, '//span[text()="5"]').click()

    def press_button_6(self):
        self._driver.find_element(By.XPATH, '//span[text()="6"]').click()

    def press_button_7(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()

    def press_button_8(self):
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()

    def press_button_9(self):
        self._driver.find_element(By.XPATH, '//span[text()="9"]').click()

    def press_button_point(self):
        self._driver.find_element(By.XPATH, '//span[text()="."]').click()

    def press_button_plus(self):
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()

    def press_button_minus(self):
        self._driver.find_element(By.XPATH, '//span[text()="-"]').click()

    def press_button_umnogenie(self):
        self._driver.find_element(By.XPATH, '//span[text()="x"]').click()

    def press_button_delenie(self):
        self._driver.find_element(By.XPATH, '//span[text()="÷"]').click()

    def press_button_rezult(self):
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()

    def waiter_resuit(self):
        WebDriverWait(self._driver, 50, 0.1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))

    def result(self):
        result = self._driver.find_element(By.CSS_SELECTOR, "div.screen").text
        return result

    def clouse_driver(self):
        self._driver.quit()   