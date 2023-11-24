from base.BasePage import BasePage
import pages.PageElements as pe

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_search_field(self):
        BasePage.is_displayed(self, pe.naver_search_field)

    def check_account_container(self):
        BasePage.is_displayed(self, pe.account_container)

    def check_login_info_text(self):
        BasePage.is_displayed(self, pe.login_info_text)

    def check_login_button(self):
        BasePage.is_displayed(self, pe.login_button)

    def check_find_id_text(self):
        BasePage.is_displayed(self, pe.login_find_id)

    def check_find_password_text(self):
        BasePage.is_displayed(self, pe.login_find_password)

    def check_register_text(self):
        BasePage.is_displayed(self, pe.login_register)