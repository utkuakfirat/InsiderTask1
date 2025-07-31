import pytest
from pages.base_page import *

@pytest.mark.usefixtures("setup")
class CheckjobPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_new_window(self):
     self.switch_to_window(1)


     
