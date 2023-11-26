from base.BasePage import BasePage
import pages.PageElements as pe

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def input_id(self, text):
        if text == "<empty>":
            text == ""
        BasePage.input_element(self, pe.id_input_field, text)
        
    def input_password(self, text):
        if text == "<empty>":
            text == ""
        BasePage.input_element(self, pe.password_input_field, text)

    def click_login_page_button(self):
        BasePage.click_element(self, pe.login_page_button)

    def check_error_message(self, error_message):
        BasePage.is_displayed(self, pe.error_message)
