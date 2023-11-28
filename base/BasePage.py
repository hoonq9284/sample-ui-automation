import os
import time
from selenium.webdriver.common.by import By

waitTime = 10
BASE_DIR = os.getcwd()

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def maximize_window(self):
        self.driver.maximize_window()

    # 모든 창 핸들을 가져오고, 현재 활성화 된 핸들을 제외한 창으로 이동
    def switch_to_window(self):
        self.driver.implicitly_wait(waitTime)
        current_window_handle = self.driver.current_window_handle
        window_handles = self.driver.window_handles
        for handle in window_handles:
            if handle != current_window_handle:
                self.driver.switch_to.window(handle)
                break
            
    def highlight(self, element, effect_time, color, border):
        driver = element._parent

        def apply_style(s):
            driver.implicitly_wait(waitTime)
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

        original_style = element.get_attribute('style')
        apply_style(f"border: {border}px solid {color};")
        time.sleep(effect_time)
        apply_style(original_style)

    def is_displayed(self, locator):
        self.driver.implicitly_wait(waitTime)
        try:
            element = self.driver.find_element(by=By.XPATH, value=locator)
            self.highlight(element, 0.1, "#FF0000", 3)
            element.is_displayed()
            return True
        except Exception as e:
            print(e)
            return False

    def click_element(self, locator):
        self.driver.implicitly_wait(waitTime)
        try:
            element = self.driver.find_element(by=By.XPATH, value=locator)
            self.highlight(element, 0.1, "#FF0000", 3)
            element.click()
            return True
        except Exception as e:
            print(e)
            return False
            
    def input_element(self, locator, text):
        self.driver.implicitly_wait(waitTime)
        try:
            element = self.driver.find_element(by=By.XPATH, value=locator)
            self.highlight(element, 0.1, "#FF0000", 3)
            element.send_keys(text)
            return True
        except Exception as e:
            print(e)
            return False
