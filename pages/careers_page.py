import pytest
from pages.base_page import *
from constants.careers_page_locator import *

@pytest.mark.usefixtures("setup")
class CareersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    URL = "https://useinsider.com/careers/"

    def open_in_new_tab(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get(self.URL)

    def hover_see_all_teams(self):
        self.hover_over_element(SEE_ALL_TEAMS)

    def click_see_all_teams(self):
        self.click_to_element(SEE_ALL_TEAMS)

    def all_teams_check(self):
        self.get_text(CHECK_ALL_TEAMS)
          
    def product_design_wait(self):
        self.hover_over_element(PRODUCT_DESIGN_WAIT)

    def hover_our_locations_block(self):
        self.hover_over_element(OUR_LOCATIONS_BLOCK)
    
    def check_location_Info(self):
        self.click_to_element(LOCATION_INFO)

    def hover_life_at_insider_block(self):
        self.hover_over_element(LIFE_AT_INSIDER_BLOCK)
    
    #Life at Insider” adlı bölümün görünürlüğünü kontrol edip oradaki slider ya da resim öğelerini kontrol ediyoruz.
    def check_life_at_insider_picture(self):
       block = self.wait_for_element_to_be_visible(LIFE_AT_INSIDER_BLOCK)
       self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", block)
       time.sleep(2)
       return self.wait_for_elements_to_be_present(SWIPER_ITEMS, timeout=10)
    def click_see_all_teams(self):
     try:
        for i in range(0, 3000, 300):
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(0.3)
        
      #See All Teams” butonunu bulma ve tıklama işlemi
        element = self.wait_for_element_to_be_visible(SEE_ALL_TEAMS, timeout=15)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", element)
     except Exception as e:
        print(f"[HATA] See All Teams tıklanamadı: {e}")
        raise



