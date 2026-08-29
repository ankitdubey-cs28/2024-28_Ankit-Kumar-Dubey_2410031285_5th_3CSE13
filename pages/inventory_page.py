from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class InventoryPage:

    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, "inventory_item_desc")
    ADD_TO_CART = (By.XPATH, "//button[text()='Add to cart']")
    REMOVE = (By.XPATH, "//button[text()='Remove']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    FILTER = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        self.driver = driver

    def get_product_names(self):
        products = self.driver.find_elements(*self.PRODUCT_NAME)
        names = []

        for product in products:
            names.append(product.text)

        return names
    

    def get_product_prices(self):

        prices = self.driver.find_elements(*self.PRODUCT_PRICE)

        product_prices = []

        for price in prices:
            product_prices.append(price.text)

        return product_prices
    

    def get_product_descriptions(self):

        descriptions = self.driver.find_elements(*self.PRODUCT_DESCRIPTION)

        product_descriptions = []

        for description in descriptions:
            product_descriptions.append(description.text)

        return product_descriptions
    
    def add_first_product_to_cart(self):

     add_buttons = self.driver.find_elements(*self.ADD_TO_CART)

     add_buttons[0].click()

    def add_all_products_to_cart(self):

        add_buttons = self.driver.find_elements(*self.ADD_TO_CART)

        for button in add_buttons:
            button.click()

    def remove_first_product(self):

        self.driver.find_element(*self.REMOVE).click()

    def get_cart_count(self):

     return self.driver.find_element(*self.CART_BADGE).text
    def click_cart(self):

        self.driver.find_element(*self.CART_ICON).click()
    def select_filter(self, value):

        dropdown = Select(self.driver.find_element(*self.FILTER))

        dropdown.select_by_visible_text(value)