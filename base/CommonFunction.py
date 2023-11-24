import config.config
from base.BasePage import BasePage
from selenium import webdriver

class CommonFunction(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_new_window(self):
        BasePage.execute_script_window_open(self)

    def maximize_window(self):
        BasePage.maximize_window(self)

    def switch_to_window(self, switch_number):
        BasePage.switch_to_window(self, switch_number)
        
    def refresh_page(self):
        BasePage.refresh_page(self)

    def open_new_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.config.BASE_URL)
