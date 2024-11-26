from selenium.webdriver.common.by import By

class MainPage_bonigarcia:
    
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def add_first_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(term)

    def add_last_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(term)

    def add_address(self, term):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(term)

    def add_email(self, term):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(term)

    def add_phone(self, term):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(term)

    def add_zipcode(self, term):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys(term)

    def add_city(self, term):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(term)

    def add_country(self, term):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(term)

    def add_jobposition(self, term):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(term)

    def add_company(self, term):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(term)

    def push_button(self):
        self._driver.find_element(By.CSS_SELECTOR, "button.btn-outline-primary").click()

    def get_attribute_class_first_name(self):
        clas = self._driver.find_element(By.ID, "first-name").get_attribute("class")
        return clas

    def get_attribute_class_last_name(self):
        clas = self._driver.find_element(By.ID, "last-name").get_attribute("class")
        return clas

    def get_attribute_class_address(self):
        clas = self._driver.find_element(By.ID, "address").get_attribute("class")
        return clas

    def get_attribute_class_email(self):
        clas = self._driver.find_element(By.ID, "e-mail").get_attribute("class")
        return clas

    def get_attribute_class_phone(self):
        clas = self._driver.find_element(By.ID, "phone").get_attribute("class")
        return clas

    def get_attribute_class_zipcode(self):
        clas = self._driver.find_element(By.ID, "zip-code").get_attribute("class")
        return clas

    def get_attribute_class_city(self):
        clas = self._driver.find_element(By.ID, "city").get_attribute("class")
        return clas

    def get_attribute_class_country(self):
        clas = self._driver.find_element(By.ID, "country").get_attribute("class")
        return clas

    def get_attribute_class_jobposition(self):
        clas = self._driver.find_element(By.ID, "job-position").get_attribute("class")
        return clas

    def get_attribute_class_company(self):
        clas = self._driver.find_element(By.ID, "company").get_attribute("class")
        return clas
    
    def clouse_driver(self):
        self._driver.quit()