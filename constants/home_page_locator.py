from selenium.webdriver.common.by import By

BASE_URL = "https://useinsider.com/"
CLICK_COMPANY_BUTTON = (By.CSS_SELECTOR,"li:nth-of-type(6) > a#navbarDropdownMenuLink")
Insider_logo_check = (By.CSS_SELECTOR, "a.navbar-brand.d-flex.flex-row.align-items-center[href='/']")
AGENT_ONE_TEXT = (By.CSS_SELECTOR, "div.slide-text > span")
SEE_ALL_TEAMS = (By.CSS_SELECTOR, ".btn.btn-outline-secondary.loadmore.mt-5.mx-auto.py-3.rounded.text-medium")
TEAMS_BLOCK = (By.CSS_SELECTOR, "[class='job-item col-12 col-lg-4 mt-5']")
OUR_LOCATIONS_BLOCK = (By.CSS_SELECTOR, ".category-title-media.ml-0")
LOCATIONS_ITEMS = (By.CSS_SELECTOR, "ul.glide__slides > li.glide__slide")
LIFE_AT_INSIDER_BLOCK = (By.CSS_SELECTOR,
    ".elementor-element.elementor-element-21cea83.elementor-widget.elementor-widget-heading "
    ".elementor-heading-title.elementor-size-default")
CLICK_ACCEPT_ALL_BUTTON = (By.ID,"wt-cli-accept-all-btn")
CLICK_CAREERS_BUTTON = (By.CSS_SELECTOR,".new-menu-dropdown-layout-6-mid-container a:nth-of-type(2)")