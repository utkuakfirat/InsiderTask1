import pytest
from pages.base_page import *
from constants.home_page_locator import *

@pytest.mark.usefixtures("setup")
class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_homepage_opened(self, timeout=10):
      return self.is_visible(Insider_logo_check, timeout)

 
    def accept_cookies(self, timeout=5):
        """Çerez kabul butonunu tıklar, buton yoksa timeout sonrası hata vermeden devam eder."""
        try:
            button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.Cookies_accept)
            )
            button.click()
        except TimeoutException:
            print("Çerez butonu tıklanamadı veya görünmüyor.")

    def is_title_text_present(self, expected_text, timeout=10):
       try:
        WebDriverWait(self.driver, timeout).until(EC.title_contains(expected_text))
        return True
       except:
        return False

    def click_accept_all_button(self):
        self.click_to_element(CLICK_ACCEPT_ALL_BUTTON)

    def click_company_button(self):
        self.click_to_element(CLICK_COMPANY_BUTTON)
        
    def click_careers_button(self):
        self.click_to_element(CLICK_CAREERS_BUTTON)