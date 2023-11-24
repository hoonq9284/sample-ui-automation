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
