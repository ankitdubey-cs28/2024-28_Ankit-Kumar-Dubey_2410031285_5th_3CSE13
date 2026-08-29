from selenium import webdriver

class Browser:

    @staticmethod
    def start_browser():

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(10)

        return driver

    @staticmethod
    def close_browser(driver):
        driver.quit()