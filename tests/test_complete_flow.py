import time

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.menu_page import MenuPage

from utilities.browser import Browser
from test_data.credentials import USERNAME, PASSWORD

# ==========================================
# Start Browser
# ==========================================

driver = Browser.start_browser()

# ==========================================
# Create Objects
# ==========================================

login = LoginPage(driver)
inventory = InventoryPage(driver)
cart = CartPage(driver)
checkout = CheckoutPage(driver)
menu = MenuPage(driver)

# ==========================================
# Open Website
# ==========================================

print("Opening Website...")
login.open_website()
time.sleep(2)

# ==========================================
# Login
# ==========================================

print("Logging In...")
login.login(USERNAME, PASSWORD)
time.sleep(2)

assert "inventory.html" in driver.current_url
print("✅ Login Assertion Passed")

# ==========================================
# FILTER AUTOMATION
# ==========================================

print("\nApplying Filter : Name (A to Z)")
inventory.select_filter("Name (A to Z)")
time.sleep(3)

print("\nApplying Filter : Name (Z to A)")
inventory.select_filter("Name (Z to A)")
time.sleep(3)

print("\nApplying Filter : Price (low to high)")
inventory.select_filter("Price (low to high)")
time.sleep(3)

print("\nApplying Filter : Price (high to low)")
inventory.select_filter("Price (high to low)")
time.sleep(3)

# ==========================================
# Product Details
# ==========================================

print("\n========== PRODUCT NAMES ==========")
for product in inventory.get_product_names():
    print(product)

print("\n========== PRODUCT PRICES ==========")
for price in inventory.get_product_prices():
    print(price)

print("\n========== PRODUCT DESCRIPTIONS ==========")
for description in inventory.get_product_descriptions():
    print(description)

time.sleep(2)

# ==========================================
# Add First Product
# ==========================================

print("\nAdding First Product...")
inventory.add_first_product_to_cart()

time.sleep(2)

assert inventory.get_cart_count() == "1"
print("✅ Product Added Assertion Passed")

print("Cart Count :", inventory.get_cart_count())

time.sleep(2)

# ==========================================
# Open Cart
# ==========================================

print("\nOpening Cart...")
inventory.click_cart()

time.sleep(2)

assert "cart.html" in driver.current_url
print("✅ Cart Page Assertion Passed")

# ==========================================
# Cart Details
# ==========================================

assert cart.get_product_name() != ""
assert cart.get_product_price() != ""
assert cart.get_quantity() == "1"
assert cart.get_product_description() != ""

print("✅ Cart Details Assertion Passed")

print("\n========== CART DETAILS ==========")
print("Product :", cart.get_product_name())
print("Price :", cart.get_product_price())
print("Quantity :", cart.get_quantity())
print("Description :", cart.get_product_description())

time.sleep(2)

# ==========================================
# Checkout
# ==========================================

print("\nCheckout...")
cart.click_checkout()

time.sleep(2)

assert "checkout-step-one.html" in driver.current_url
print("✅ Checkout Step One Assertion Passed")
# ==========================================
# Fill Checkout Details
# ==========================================

print("\nFilling Checkout Details...")

checkout.fill_checkout_details(
    "Ankit",
    "Dubey",
    "221001"
)

time.sleep(2)

checkout.click_continue()

time.sleep(2)

# ==========================================
# Checkout Step Two Assertion
# ==========================================

assert "checkout-step-two.html" in driver.current_url
print("✅ Checkout Step Two Assertion Passed")

# ==========================================
# Finish Order
# ==========================================

print("\nFinishing Order...")

checkout.click_finish()

time.sleep(2)

# ==========================================
# Order Success Assertion
# ==========================================

assert checkout.get_success_message() == "Thank you for your order!"
print("✅ Order Success Assertion Passed")

print("\n========== ORDER STATUS ==========")
print(checkout.get_success_message())

time.sleep(2)

# ==========================================
# Back Home
# ==========================================

print("\nReturning To Home Page...")

checkout.click_back_home()

time.sleep(2)

assert "inventory.html" in driver.current_url
print("✅ Back Home Assertion Passed")

# ==========================================
# MENU AUTOMATION
# ==========================================

print("\nOpening Menu...")
menu.open_menu()

time.sleep(2)

print("Reset App State...")
menu.click_reset_app_state()

time.sleep(2)

print("Logging Out...")
menu.click_logout()

time.sleep(2)

# ==========================================
# Logout Assertion
# ==========================================

assert "saucedemo.com" in driver.current_url
print("✅ Logout Assertion Passed")

print("\n🎉 ALL ASSERTIONS PASSED")
print("🎉 COMPLETE AUTOMATION FLOW EXECUTED SUCCESSFULLY")

input("\nPress Enter To Close Browser...")

Browser.close_browser(driver)