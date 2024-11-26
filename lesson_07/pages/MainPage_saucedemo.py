from selenium.webdriver.common.by import By

class MainPage_saucedemo:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def enter_username(self, trem):
            self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(trem)


    def enter_password(self, trem):
             self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(trem)

    def login(self):
          self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def add_element_1(self):
          self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    def add_element_2(self):
          self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

    def add_element_3(self):
          self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def shopping_cart_container(self):
          self._driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()

    def checkout(self):
          self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    def enter_first_name(self,trem):
          self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(trem)

    def enter_last_name(self,trem):
          self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(trem)

    def enter_postal_code(self,trem):
          self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(trem)

    def enter_continue(self):
          self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def enter_total_label(self):
          Total = self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
          return Total
    
    def clouse_driver(self):
        self._driver.quit() 
