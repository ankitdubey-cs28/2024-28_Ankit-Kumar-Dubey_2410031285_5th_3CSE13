from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utilities.browser import Browser
from test_data.credentials import USERNAME, PASSWORD

# Start Browser
driver = Browser.start_browser()

# Create Objects
login = LoginPage(driver)
inventory = InventoryPage(driver)

# Open Website
login.open_website()

# Login
login.login(USERNAME, PASSWORD)

# ----------------------------
# Product Details
# ----------------------------

print("========== Product Names ==========")
print(inventory.get_product_names())

print("\n========== Product Prices ==========")
print(inventory.get_product_prices())

print("\n========== Product Descriptions ==========")
print(inventory.get_product_descriptions())

# ----------------------------
# Add First Product
# ----------------------------

inventory.add_first_product_to_cart()

print("\nFirst Product Added Successfully")

# ----------------------------
# Cart Count
# ----------------------------

count = inventory.get_cart_count()

print("Cart Count :", count)

# ----------------------------
# Open Cart
# ----------------------------

inventory.click_cart()

print("Cart Page Opened Successfully")

input("\nPress Enter to close browser...")

Browser.close_browser(driver)