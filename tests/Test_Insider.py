import pytest
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.quality_assurance_page import QualityAssurancePage
from pages.check_job_page import CheckjobPage
from constants.home_page_locator import *
from constants.careers_page_locator import *
from constants.quality_assurance_page_locator import *
import time


@pytest.mark.usefixtures("setup")
class TestInsider:

    def test_insider(self):
        base = BasePage(self.driver)
        home = HomePage(self.driver)
        careers = CareersPage(self.driver)
        quality_assurance = QualityAssurancePage(self.driver)
        job = CheckjobPage(self.driver)


        # Çerez tercihi "kabul et" olarak seçildi.
        home.click_accept_all_button()

        # Ana sayfa başarılı şekilde yükleniyor mu kontrol edilir.
        assert self.driver.current_url == "https://useinsider.com/", f"Expected 'https://useinsider.com/', but found '{self.driver.current_url}'"
        base.screenshot("screenshot/home_page.png")

        #  Insider logosunun ana sayfada yüklendiği ve görüntülendiği doğrulanır.
        assert base.is_visible(Insider_logo_check), "Expected Insider logo to be visible, but it wasn't."

        # Ana sayfada yer alan belirli bir yazı metninin doğru görüntülendiği kontrol edilir.
        assert home.is_text_visible(AGENT_ONE_TEXT, "Launching Agent One™"), \
        "Beklenen metin sayfada görünmüyor"

        # "Company" menüsünün görüntülendiği doğrulanır ve ardından bu butonuna tıklanır.
        assert (company_button := base.wait_for_element_to_be_visible(CLICK_COMPANY_BUTTON)).text == "Company", f"Expected: 'Company', but found: '{company_button.text}'"
        home.click_company_button()

        # "Careers" butonunun görüntülendiği kontrol edilir ve "Careers" butonuna tıklanır.
        assert (careers_button := base.wait_for_element_to_be_visible(CLICK_CAREERS_BUTTON)).text == "Careers", f"Expected: 'Careers', but found: '{careers_button.text}'"
        home.click_careers_button()

        # "Careers" sayfasının başarılı bir şekilde açıldığı kontrol edilir.
        assert self.driver.current_url == "https://useinsider.com/careers/", \
        f"Expected 'https://useinsider.com/careers/', but found '{self.driver.current_url}'"

        #  Yeni sekmede açılan sayfanın URL'sinin beklenen URL ile eşleşip eşleşmediği kontrol edilir.
        assert self.driver.current_url == careers.URL, f"Expected '{careers.URL}', but found '{self.driver.current_url}'"

        # "See All Teams" butonunun sayfada yer aldığı kontrol edilir.
        careers.hover_see_all_teams()
        assert base.get_text(SEE_ALL_TEAMS) == "See all teams"
        careers.click_see_all_teams()

        # Sayfa aşağı kaydırılır ve team bloklarının görüntülendiği kontrol edilir.
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        teams_block = base.wait_for_elements_to_be_visible(TEAMS_BLOCK)
        assert len(teams_block) == 15, f"Expected 15 blocks, found {len(teams_block)}"

        # Yeni açılan blokta başlık metninin doğru şekilde görüntülendiği kontrol edilir.
        all_teams_text = base.get_text(CHECK_ALL_TEAMS)
        assert all_teams_text == "Customer Success"
        
        #  Sayfa kaydırılarak "Our Locations" bloğuna ulaşılır ve bu bloğun sayfada görünür olduğu doğrulanır.
        careers.hover_our_locations_block()
        assert (our_locations_block := base.wait_for_element_to_be_visible(OUR_LOCATIONS_BLOCK)).text == "Our Locations", f"Expected: 'Our Locations', but found: {our_locations_block}"

        #Locations bölümünde yer alan ülkelerin doğru şekilde görüntülendiği ve listelendiği doğrulanır.
        careers.check_location_Info()
        location_info = base.wait_for_element_to_be_visible(LOCATION_INFO)
        assert location_info.text in ["Istanbul", "New York", "London", "Dubai"], f"Unexpected location: {location_info.text}"
        
        # Sayfa kaydırılarak "Life at Insider" bloğuna ulaşılır ve bloğun görünür olduğu doğrulanır.
        careers.hover_life_at_insider_block()
        assert (life_at_insider_block := base.wait_for_element_to_be_visible(LIFE_AT_INSIDER_BLOCK)).text == "Life at Insider", f"Expected: 'Life at Insider', but found: {life_at_insider_block}'"
        
        # "Life at Insider" bloğundaki resimlerin varlığı ve görüntülenmesi kontrol edilir.
        careers.hover_life_at_insider_block()   
        swiper_items = careers.check_life_at_insider_picture()
        assert len(swiper_items) >= 5, f"Swiper'da yeterli içerik görünmüyor, bulunan: {len(swiper_items)}"
        self.driver.save_screenshot("screenshot/life_at_insider_swiper.png")

        # Swiper kartlarının yüklendiği ve sayfada görüntülendiği kontrol edilir.
        swiper_items = careers.check_life_at_insider_picture()
        assert len(swiper_items) > 0, "Swiper öğeleri görünmüyor."

        # "https://useinsider.com/careers/quality-assurance/" linkinin yeni pencerede açıldığı kontrol edilir.
        quality_assurance.new_url("https://useinsider.com/careers/quality-assurance/")
        assert self.driver.current_url == "https://useinsider.com/careers/quality-assurance/", f"Expected 'https://useinsider.com/careers/quality-assurance/', but found '{self.driver.current_url}'"
        base.screenshot("screenshot/new_url_page.png")

        # "See All QA Jobs" butonunun görüntülendiği doğrulanır ve "See All QA Jobs" butonuna tıklanabildiği kontrol edilir.
        assert (see_all_qa_jobs := base.wait_for_element_to_be_visible(SEE_ALL_QA_JOBS)).text == "See all QA jobs", f"Expected: 'See all QA jobs', but found: {see_all_qa_jobs}"
        quality_assurance.click_see_all_qa_jobs()

        #  Sayfa başlığının "Insider Open Positions | Insider" ile eşleştiği doğrulanır.
        assert (positions_page_title := self.driver.title) == "Insider Open Positions | Insider", f"Expected title: 'Insider Open Positions | Insider', but found: '{positions_page_title}'"
        
        # "Quality Assurance" seçeneğinin sayfada görüntülendiği beklenir.
        quality_assurance.wait_quality_assurance()

        # "Quality Assurance" seçeneğinin DOM'da varlığı ve görünürlüğü doğrulanır.
        assert (quality_assurance_title := base.wait_for_element_to_be_visible(QUALITY_ASSURANCE_TITLE)).get_attribute("title") == "Quality Assurance", f"Expected title: 'Quality Assurance', but found: '{quality_assurance_title.get_attribute('title')}'"
        
        # Lokasyonda "Istanbul, Turkey" seçeneğine tıklanır ve "Istanbul, Turkey" seçeneğinin görüntülendiği kontrol edilir.
        # Lokasyon filtrelemesi yapılır.
        quality_assurance.click_filter_by_location()
        time.sleep(1)
        quality_assurance.click_istanbul_turkey()
        selected_location = base.wait_for_element_to_be_visible(ISTANBUL_TURKEY_TITLE)
        actual_title = selected_location.get_attribute("title")
        # En az bir tanesinde 'Istanbul' geçiyor mu kontrol edilir.
        assert "Istanbul" in actual_title and ("Turkey" in actual_title or "Turkiye" in actual_title), \
        f"Unexpected location title: {actual_title}"

        #  Lokasyon ve departman isimlerinin doğru şekilde görüntülendiği kontrol edilir.
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        quality_assurance.hover_job()

        locations = base.wait_for_elements_to_be_visible(LOCATION)
        departments = base.wait_for_elements_to_be_visible(DEPARTMENT)
        positions = base.wait_for_elements_to_be_visible(POSITION)

        assert locations, "Lokasyonlar bulunamadı"
        assert departments, "Departmanlar bulunamadı"
        assert positions, "Pozisyonlar bulunamadı"

        assert "Istanbul" in locations[0].text and ("Turkey" in locations[0].text or "Turkiye" in locations[0].text), f"Beklenmeyen lokasyon: {locations[0].text}"
        assert departments[0].text == "Quality Assurance", f"Beklenen 'Quality Assurance', bulundu: {departments[0].text}"
        assert "Quality Assurance" in positions[0].text, f"Pozisyonda 'Quality Assurance' yok: {positions[0].text}"

        base.screenshot("screenshot/job_page.png")

        # "View Role" butonunun DOM'da yüklenip görünür olması beklenir, ardından tıklama işlemi gerçekleştirilir.
        quality_assurance.click_first_view_role_button()

        # Başvuru sayfasının başarıyla açıldığı kontrol edilir.
        job.get_new_window()
        assert "jobs.lever.co/useinsider" in self.driver.current_url, f"Expected 'jobs.lever.co/useinsider' to be in '{self.driver.current_url}'"
        base.screenshot("screenshot/aplication_page.png")
        
        # Lever sayfasının açıldığı ve başvuru formunun sayfada başarıyla yüklendiği, kullanıma hazır olduğu doğrulanır.
        quality_assurance.click_apply_button()
        time.sleep(2) 
        assert "apply" in self.driver.current_url, "Başvuru sayfası açılmadı"

      

