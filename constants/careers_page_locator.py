from selenium.webdriver.common.by import By

URL = "https://useinsider.com/careers/quality-assurance/"

SWIPER_ITEMS = (By.CSS_SELECTOR, ".elementor-main-swiper .swiper-slide:not(.swiper-slide-duplicate)")
LOCATION_INFO=(By.CSS_SELECTOR, ".location-info p")
CHECK_ALL_TEAMS=(By.CSS_SELECTOR, ".job-title h3")
SEE_ALL_TEAMS = (By.CSS_SELECTOR,".btn.btn-outline-secondary.loadmore.mt-5.mx-auto.py-3.rounded.text-medium")
PRODUCT_DESIGN_WAIT = (By.CSS_SELECTOR,".career-load-more.col-12.d-flex.flex-wrap.p-0 > div:nth-of-type(15)")
TEAMS_BLOCK = (By.CSS_SELECTOR, "[class='job-item col-12 col-lg-4 mt-5']")
OUR_LOCATIONS_BLOCK = (By.CSS_SELECTOR,".category-title-media.ml-0")
LIFE_AT_INSIDER_BLOCK = (By.CSS_SELECTOR,".elementor-element.elementor-element-21cea83.elementor-widget.elementor-widget-heading  .elementor-heading-title.elementor-size-default")