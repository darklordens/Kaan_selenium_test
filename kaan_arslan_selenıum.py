from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class InsiderPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()  # Tarayıcıyı tam ekran yap
        self.driver.get("https://useinsider.com/")
        # Sayfanın yüklenmesi için 10 saniye bekle
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        self.handle_cookies_and_popups()

    def handle_cookies_and_popups(self):
        # Pop-up veya cookies bildirimlerini kapat
        try:
            cookers_close = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='wt-cli-accept-all-btn' and text()='Accept All']")))
            cookers_close.click()
        except Exception as e:
            print(f"Cookie pop-up kapatılırken hata oluştu: {e}")

    def click_company(self):
        # Company sekmesine tıklama
        try:
            company = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='navbarDropdownMenuLink' and contains(text(), 'Company')]")))
            company.click()
        except Exception as e:
            print(f"Company sekmesine tıklanırken hata oluştu: {e}")

    def click_careers(self):
        # Careers sekmesine tıklama ve sayfanın yüklenmesini bekleme
        try:
            careers = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://useinsider.com/careers/']")))
            careers.click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        except Exception as e:
            print(f"Careers sekmesine tıklanırken hata oluştu: {e}")

    def click_see_all_teams(self):
        # Sayfayı aşağı kaydır ve 'See all teams' butonunu bulana kadar sürdür
        while True:
            self.driver.execute_script("window.scrollBy(0, 1000);")  # Sayfayı daha hızlı kaydır
            try:
                see_all_teams = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'See all teams')]")))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", see_all_teams)
                see_all_teams.click()
                break  # Element bulundu ve tıklandı, döngüden çık
            except Exception as e:
                print(f"'See all teams' butonuna tıklanırken hata oluştu: {e}")
                time.sleep(1)

    def go_to_qa_page(self):
        # Quality Assurance sayfasına git ve sayfanın yüklenmesini bekleme
        self.driver.get("https://useinsider.com/careers/quality-assurance/")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        self.handle_cookies_and_popups()

    def click_see_all_qa_jobs(self):
        # 'See all QA jobs' butonuna tıklama ve sayfanın yüklenmesini bekleme
        try:
            see_all_qa_jobs = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'See all QA jobs')]")))
            see_all_qa_jobs.click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        except Exception as e:
            print(f"'See all QA jobs' butonuna tıklanırken hata oluştu: {e}")

    def filter_by_location(self):
        while True:
            try:
                # Filter by Location alanına tıklama
                filter_location_arrow = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='select2-selection__arrow']")))
                filter_location_arrow.click()
                # Açılan listede 'Istanbul, Turkey' seçme
                istanbul = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Istanbul, Turkey')]")))
                istanbul.click()
                break  # 'Istanbul, Turkey' seçeneği bulundu ve seçildi
            except Exception as e:
                print(f"Filtreleme sırasında hata oluştu: {e}")
                # Eğer 'Istanbul, Turkey' seçeneği bulunamazsa tekrar tıklama yap
                try:
                    filter_location_arrow.click()
                    istanbul = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Istanbul, Turkey')]")))
                    istanbul.click()
                    break
                except:
                    # 'Istanbul, Turkey' seçeneği bulunamazsa sayfayı yenile
                    self.driver.get("https://useinsider.com/careers/open-positions/?department=qualityassurance")
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='position-list-item-wrapper bg-light']")))
        time.sleep(2)  # Filtreler sonrası bekleme
        self.driver.execute_script("window.scrollBy(0, 1000);")  # Sayfayı aşağı kaydır

    def click_view_role(self):
        # 'View Role' butonuna tıklama
        try:
            view_role = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc' and contains(@class, 'btn btn-navy rounded pt-2 pr-5 pb-2 pl-5')]")))
            view_role.click()
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            time.sleep(3)
        except Exception as e:
            print(f"'View Role' butonuna tıklanırken hata oluştu: {e}")

    def hover_over_position(self):
        # İş ilanlarının üzerine fare ile gelme
        try:
            position = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='position-list-item-wrapper bg-light']")))
            ActionChains(self.driver).move_to_element(position).perform()
        except Exception as e:
            print(f"Pozisyon üzerine fare ile gelinirken hata oluştu: {e}")



    def click_apply_for_this_job(self):
        # 'Apply for this job' butonuna tıklama
        try:
            apply_for_this_job = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@class, 'btn btn-navy rounded') and text()='Apply for this job']")))
            apply_for_this_job.click()
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            time.sleep(3)  # Açılan sayfada 3 saniye bekle

            # Apply for this job sayfasında 'Apply for this job' butonuna tıklama
            apply_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@class='postings-btn template-btn-submit shamrock' and text()='Apply for this job']")))
            apply_button.click()
            time.sleep(5)  # Sayfa yüklendikten sonra 5 saniye bekle

            self.driver.quit()  # Projeyi kapat
        except Exception as e:
            print(f"'Apply for this job' butonuna tıklanırken hata oluştu: {e}")


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    # Chrome seçeneklerini ekle - pop-up ve cookies'leri kapatma
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)
    page = InsiderPage(driver)
    page.click_company()
    page.click_careers()
    page.click_see_all_teams()
    page.go_to_qa_page()
    page.click_see_all_qa_jobs()
    page.filter_by_location()
    page.hover_over_position()
    page.click_view_role()
    page.click_apply_for_this_job()
    driver.quit()


