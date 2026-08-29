from selenium.webdriver.common.by import By
from test_data.credentials import URL


class LoginPage:

    # ===================== Locators =====================

    USERNAME_TEXTBOX = (By.ID, "user-name")
    PASSWORD_TEXTBOX = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    # ===================== Constructor =====================

    def __init__(self, driver):
        self.driver = driver

    # ===================== Methods =====================

    def open_website(self):
        self.driver.get(URL)

    def enter_username(self, username):
     textbox = self.driver.find_element(*self.USERNAME_TEXTBOX)
     textbox.clear()
     textbox.send_keys(username)

    def enter_password(self, password):
     textbox = self.driver.find_element(*self.PASSWORD_TEXTBOX)
     textbox.clear()
     textbox.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text