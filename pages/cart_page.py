from selenium.webdriver.common.by import By


class CartPage:

    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, "inventory_item_desc")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    PRODUCT_QUANTITY = (By.CLASS_NAME, "cart_quantity")

    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT = (By.ID, "checkout")
    REMOVE = (By.XPATH, "//button[text()='Remove']")

    def __init__(self, driver):
        self.driver = driver
    def get_product_name(self):
        return self.driver.find_element(*self.PRODUCT_NAME).text
    def get_product_description(self):
        return self.driver.find_element(*self.PRODUCT_DESCRIPTION).text
    def get_product_price(self):
        return self.driver.find_element(*self.PRODUCT_PRICE).text
    def get_quantity(self):
        return self.driver.find_element(*self.PRODUCT_QUANTITY).text
    def continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING).click()
    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT).click()
    def remove_product(self):
        self.driver.find_element(*self.REMOVE).click() 
    