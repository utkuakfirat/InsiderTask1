import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _wait(self, locator, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    def wait_for_element(self, locator, timeout=10):
        return self._wait(locator, EC.visibility_of_element_located, timeout)

    def wait_for_elements(self, locator, timeout=10):
        return self._wait(locator, EC.visibility_of_all_elements_located, timeout)

    def wait_for_clickable(self, locator, timeout=10):
        return self._wait(locator, EC.element_to_be_clickable, timeout)

    def click(self, locator, timeout=10):
        self.wait_for_clickable(locator, timeout).click()

    def get_text(self, locator, timeout=10):
     element = self.wait_for_element_to_be_visible(locator, timeout)
     return element.text

    def is_visible(self, locator, timeout=10):
        return self._check_element_status(locator, EC.visibility_of_element_located, timeout)

    def is_present(self, locator, timeout=10):
        return self._check_element_status(locator, EC.presence_of_element_located, timeout)

    def is_enabled(self, locator, timeout=10):
        return self._check_element_status(locator, EC.element_to_be_clickable, timeout)

    def _check_element_status(self, locator, condition, timeout):
        try:
            self._wait(locator, condition, timeout)
            return True
        except TimeoutException:
            return False
    def hover_over_element(self, locator, timeout=10):
        self.hover(locator, timeout)

    def click_to_element(self, locator, timeout=10):
        element = self.wait_for_clickable(locator, timeout)
        element.click()

    def hover(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        ActionChains(self.driver).move_to_element(element).perform()

    def hover_and_click(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def navigate_to_url(self, url):
        self.driver.get(url)

    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def screenshot(self, file_path):
        self.driver.save_screenshot(file_path)

    def sleep(self, seconds=2):
        time.sleep(seconds)

    def is_text_visible(self, locator, expected_text, timeout=10):
       try:
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return expected_text in element.text
       except:
        return False
       
    def wait_for_element_to_be_visible(self, locator, timeout=10):
      return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    

    def wait_for_elements_to_be_visible(self, locator, timeout=10):
     return WebDriverWait(self.driver, timeout).until(
        EC.visibility_of_all_elements_located(locator)
    )

    def click_to_element(self, locator, timeout=10):
     element = self.wait_for_clickable(locator, timeout)
     self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
     WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
     element.click()

    def wait_for_clickable(self, locator, timeout=10):
     return WebDriverWait(self.driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

    def wait_for_elements_to_be_present(self, locator, timeout=10):
     return WebDriverWait(self.driver, timeout).until(
        EC.presence_of_all_elements_located(locator)
    )

    def wait_for_element_to_be_visible(self, locator, timeout=10):
     return WebDriverWait(self.driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )





    
    



