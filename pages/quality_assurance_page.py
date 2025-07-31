import pytest
from pages.base_page import *
from constants.quality_assurance_page_locator import *

@pytest.mark.usefixtures("setup")
class QualityAssurancePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def new_url(self, url):
        self.navigate_to_url(url)

    def click_see_all_qa_jobs(self):
        self.click_to_element(SEE_ALL_QA_JOBS)

    def wait_quality_assurance(self):
      self.wait_for_element_to_be_visible(WAIT_QUALITY_ASSURANCE)


    def click_filter_by_location(self):
        self.click_to_element(CLICK_FILTER_BY_LOCATION)

    def click_istanbul_turkey(self):
        self.click_to_element(CLICK_ISTANBUL_TURKEY)

    def click_view_role_button(self):
        self.get_element_index(0,VIEW_ROLE_BUTTON)
        self.hover_over_element_click(VIEW_ROLE_BUTTON)

    def hover_job(self):
        self.hover_over_element(LOCATION)
        time.sleep(2)

    def click_first_view_role_button(self):
     first_button = self.wait_for_element_to_be_visible(VIEW_ROLE_BUTTON)
     actions = ActionChains(self.driver)
     actions.move_to_element(first_button).perform()
     time.sleep(0.5)
     first_button.click()
     

    def wait_until_lever_loaded(self, timeout=10):
       WebDriverWait(self.driver, timeout).until(EC.url_contains("jobs.lever.co"))

    def dismiss_cookies_if_present(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.DISMISS_BUTTON)).click()
        except Exception:
            pass


    def click_apply_button(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(APPLY_BUTTON)).click()

 
