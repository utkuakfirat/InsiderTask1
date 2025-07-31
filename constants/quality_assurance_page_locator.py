from selenium.webdriver.common.by import By

SEE_ALL_QA_JOBS = (By.CSS_SELECTOR,"#page-head > div > div > div.col-12.col-lg-7.order-2.order-lg-1 > div > div > a")
WAIT_QUALITY_ASSURANCE = (By.XPATH, "//*[@title='Quality Assurance']")
QUALITY_ASSURANCE_TITLE = (By.CSS_SELECTOR,"#select2-filter-by-department-container")
ISTANBUL_TURKEY_TITLE = (By.ID, "select2-filter-by-location-container")
LOCATION = (By.CSS_SELECTOR,"#jobs-list > div > div > div")
POSITION = (By.XPATH,"//*[@id='jobs-list']/div/div/p")
DEPARTMENT = (By.CSS_SELECTOR,"#jobs-list > div > div > span")
CLICK_FILTER_BY_LOCATION = (By.CSS_SELECTOR,"#select2-filter-by-location-container > span")
CLICK_ISTANBUL_TURKEY = (By.XPATH, "/html/body/span/span/span[2]/ul/li[2]")
VIEW_ROLE_BUTTON = (By.CSS_SELECTOR,"a.btn.btn-navy.rounded.pt-2.pr-5.pb-2.pl-5")
APPLY_BUTTON = (By.CSS_SELECTOR, "a.postings-btn.template-btn-submit.shamrock")