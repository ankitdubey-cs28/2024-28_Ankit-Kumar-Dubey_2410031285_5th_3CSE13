import time

from pages.login_page import LoginPage
from utilities.browser import Browser

driver = Browser.start_browser()

login = LoginPage(driver)

# ==============================
# Open Website
# ==============================

login.open_website()
time.sleep(2)

# ==============================
# Test Case 1
# Empty Username
# ==============================

print("\n========== TEST CASE 1 ==========")
print("Empty Username")

login.login("", "secret_sauce")

assert login.get_error_message() == "Epic sadface: Username is required"
print("✅ Passed")

time.sleep(2)
driver.refresh()

# ==============================
# Test Case 2
# Empty Password
# ==============================

print("\n========== TEST CASE 2 ==========")
print("Empty Password")

login.login("standard_user", "")

assert login.get_error_message() == "Epic sadface: Password is required"
print("✅ Passed")

time.sleep(2)
driver.refresh()

# ==============================
# Test Case 3
# Wrong Username & Password
# ==============================

print("\n========== TEST CASE 3 ==========")
print("Wrong Username & Password")

login.login("abcd", "12345")

assert login.get_error_message() == "Epic sadface: Username and password do not match any user in this service"
print("✅ Passed")

time.sleep(2)
driver.refresh()

# ==============================
# Test Case 4
# Locked User
# ==============================

print("\n========== TEST CASE 4 ==========")
print("Locked User")

login.login("locked_out_user", "secret_sauce")

assert login.get_error_message() == "Epic sadface: Sorry, this user has been locked out."
print("✅ Passed")

time.sleep(2)

print("\n🎉 ALL INVALID LOGIN TESTS PASSED")

input("\nPress Enter To Close Browser...")

Browser.close_browser(driver)