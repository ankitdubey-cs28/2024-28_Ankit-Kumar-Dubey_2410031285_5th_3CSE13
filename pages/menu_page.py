from selenium.webdriver.common.by import By


class MenuPage:


    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    CLOSE_MENU_BUTTON = (By.ID, "react-burger-cross-btn")

    ALL_ITEMS = (By.ID, "inventory_sidebar_link")
    ABOUT = (By.ID, "about_sidebar_link")
    LOGOUT = (By.ID, "logout_sidebar_link")
    RESET_APP_STATE = (By.ID, "reset_sidebar_link")

   
    def __init__(self, driver):
        self.driver = driver


    def open_menu(self):
        self.driver.find_element(*self.MENU_BUTTON).click()


    def close_menu(self):
        self.driver.find_element(*self.CLOSE_MENU_BUTTON).click()


    def click_all_items(self):
        self.driver.find_element(*self.ALL_ITEMS).click()

    
    def click_about(self):
        self.driver.find_element(*self.ABOUT).click()

    

    def click_logout(self):
        self.driver.find_element(*self.LOGOUT).click()


    def click_reset_app_state(self):
        self.driver.find_element(*self.RESET_APP_STATE).click()