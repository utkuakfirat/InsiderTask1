import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from constants.home_page_locator import BASE_URL


@pytest.fixture
def setup(request):
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-infobars")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(BASE_URL)
    
    request.cls.driver = driver

    yield driver
    driver.quit()