import scrapy
from selenium import webdriver

from ..items import ExitoSeleniumItem

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import NoSuchElementException

class ExitoTelevisoresSpider(scrapy.Spider):

    name = 'exito_televisores'
    allowed_domains = ['exito.com']
    start_urls = ['https://www.exito.com/tecnologia/televisores']
    # start_urls = ['https://www.exito.com/mercado/vinos-y-licores/vinos']

    paginations = 5


    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}

        chrome_options.add_experimental_option("prefs",prefs)
        chrome_options.add_argument("--start-maximized")
        
        # chrome_options.add_argument("window-size=1920,1080")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)


    def parse(self, response):
        response = self.driver.get(response.url)
        
        for i in range(self.paginations):
            try:
                next_page = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,".mt3 div.vtex-button__label"))
                )

                next_page.click()

                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div.pointer.pt3.pb4.flex.flex-column.h-100"))
                )

                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR,"span.vtex-store-components-3-x-productBrand"))
                )

                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR,".search-result-exito-vtex-components-selling-price span"))
                )
            except :
                break

        item = ExitoSeleniumItem()

        

        articulos = self.driver.find_elements_by_css_selector("div.pointer.pt3.pb4.flex.flex-column.h-100")

        for articulo in articulos:

            item["nombre"] = articulo.find_element_by_css_selector("span.vtex-store-components-3-x-productBrand").text
            

            try:
                item["precio_sin_descuento"]    = articulo.find_element_by_css_selector(".search-result-exito-vtex-components-list-price span").text
            except NoSuchElementException:
                item["precio_sin_descuento"]    = ""

            try:
                item["precio_aliados"]          = articulo.find_element_by_css_selector(".search-result-exito-vtex-components-allies-discount span").text
            except NoSuchElementException:
                item["precio_aliados"]          = ""
            
            try:
                item["spot_price"]              = articulo.find_element_by_css_selector(".search-result-exito-vtex-components-selling-price span").text
            except NoSuchElementException:
                item["spot_price"]              = ""
            


            yield item


        self.driver.close()
