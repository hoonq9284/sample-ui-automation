import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

waitTime = 10
BASE_DIR = os.getcwd()

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def maximize_window(self):
        self.driver.maximize_window()

    # 요소가 표시될 때까지 대기하는 함수
    def web_driver_wait(self, locator):
        try:
            WebDriverWait(self.driver, waitTime).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
        except TimeoutException:
            print(f"TimeoutException 발생 : 엘리먼트를 최대 {waitTime}초 만큼 기다렸지만 찾을 수 없습니다.")

    # 새 창이 열렸을 때, 해당 윈도우로 포커스
    def switch_to_window(self, number):
        self.driver.switch_to.window(self.driver.window_handles[number])

    # 엘리먼트 상호작용할 때, 하이라이팅 적용
    def highlight(self, element, effect_time, color, border):
        driver = element._parent
        def apply_style(s):
            driver.implicitly_wait(waitTime)
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
        original_style = element.get_attribute('style')
        apply_style(f"border: {border}px solid {color};")
        time.sleep(effect_time)
        apply_style(original_style)

    # 엘리먼트를 찾고 이를 element 변수에 반환
    def find_element(self, locator):
        """
        엘리먼트가 화면에 표시되는 지 확인하고, 이를 element 변수에 할당하여 반환
        :param locator:
        :return:
        """
        self.web_driver_wait(locator)
        try:
            element = self.driver.find_element(by=By.XPATH, value=locator)
            self.highlight(element, 0.1, "#FF0000", 3)
            return element
        except NoSuchElementException as e:
            print(f"NoSuchElementException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트를 DOM에서 찾을 수 없습니다. 상세 정보 - {e}")
            assert False

    # 엘리먼트가 화면에 표시되는 지 확인
    def is_displayed(self, locator):
        """
        엘리먼트가 화면에 표시되는 지 확인
        (XPATH 경로를 인자로 받음)
        :param locator:
        :return:
        """
        self.web_driver_wait(locator)
        try:
            element = self.driver.find_element(by=By.XPATH, value=locator)
            self.highlight(element, 0.1, "#FF0000", 3)
            element.is_displayed()
            return True
        except NoSuchElementException as e:
            print(f"NoSuchElementException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트를 DOM에서 찾을 수 없습니다. 상세 정보 - {e}")
            assert False
        except StaleElementReferenceException as e:
            print(f"StaleElementReferenceException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트와의 참조가 더 이상 유효하지 않습니다. 상세 정보 - {e}")
            assert False

    # 엘리먼트를 클릭
    def click_element(self, locator):
        """
        엘리먼트를 찾고, 클릭
        (XPATH 경로를 인자로 받음)
        :param locator:
        :return:
        """
        self.web_driver_wait(locator)
        try:
            element = self.driver.find_element(by=By.XPATH, value=locator)
            self.highlight(element, 0.1, "#FF0000", 3)
            element.click()
            return True
        except NoSuchElementException as e:
            print(f"NoSuchElementException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트를 DOM에서 찾을 수 없습니다. 상세 정보 - {e}")
            assert False
        except ElementClickInterceptedException as e:
            print(f"ElementClickInterceptedException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트를 클릭할 수 없습니다. 상세 정보 - {e}")
            assert False
        except StaleElementReferenceException as e:
            print(f"StaleElementReferenceException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트와의 참조가 더 이상 유효하지 않습니다. 상세 정보 - {e}")
            assert False
        except ElementNotInteractableException as e:
            print(f"ElementNotInteractableException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트는 현재 상호작용할 수 없는 상태입니다. 상세 정보 - {e}")
            assert False

    # 엘리먼트에 입력
    def input_element(self, locator, text):
        """
        엘리먼트를 찾고, 데이터 입력
        (XPATH 경로와 입력할 데이터를 인자로 받음)
        :param locator:
        :param text:
        :return:
        """
        self.web_driver_wait(locator)
        try:
            element = self.driver.find_element(by=By.XPATH, value=locator)
            self.highlight(element, 0.1, "#FF0000", 3)
            element.send_keys(text)
            return True
        except NoSuchElementException as e:
            print(f"NoSuchElementException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트를 DOM에서 찾을 수 없습니다. 상세 정보 - {e}")
            assert False
        except StaleElementReferenceException as e:
            print(f"StaleElementReferenceException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트와의 참조가 더 이상 유효하지 않습니다. 상세 정보 - {e}")
            assert False
        except ElementNotInteractableException as e:
            print(f"ElementNotInteractableException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트는 현재 상호작용할 수 없는 상태입니다. 상세 정보 - {e}")
            assert False

    # 데이터 2개를 인자로 받고, 서로 비교
    def assert_text(expected, result):
        """
        result 와 expected 가 같은지 비교
        :param expected: 예상결과
        :param result:  실제값
        :return:
        """
        assert result == expected, "예상 텍스트(Expected) : " + expected + "\n 실제 텍스트(result) : " + result
