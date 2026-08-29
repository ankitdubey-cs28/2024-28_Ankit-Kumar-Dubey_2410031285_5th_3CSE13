from pages.login_page import LoginPage
from utilities.browser import Browser
from test_data.credentials import USERNAME, PASSWORD


# Browser Start
driver = Browser.start_browser()

# Login Page ka Object
login = LoginPage(driver)

# Website Open
login.open_website()

# Login
login.login(USERNAME, PASSWORD)

# Verify Login
if "inventory" in driver.current_url:
    print("✅ Login Successful")
else:
    print("❌ Login Failed")
#input("Press Enter to close browser...")

# Browser Close
Browser.close_browser(driver)