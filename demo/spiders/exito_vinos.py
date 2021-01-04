import scrapy
from selenium import webdriver

from time import sleep

from ..items import ExitoVinos

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import NoSuchElementException

from datetime import datetime


class ExitoVinosSpider(scrapy.Spider):

    name = 'exito_vinos'
    allowed_domains = ['exito.com']
    start_urls = ['https://www.exito.com/mercado/vinos-y-licores/vinos']

    paginations = 5
    ciudad = "Medellín"


    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}

        chrome_options.add_experimental_option("prefs",prefs)
        chrome_options.add_argument("--start-maximized")
        
        # chrome_options.add_argument("window-size=1920,1080")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)


    def parse(self, response):
        response = self.driver.get(response.url)

        geo_text = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.ID,"react-select-2-input"))
                )
        geo_text.send_keys(f'{self.ciudad}')
        geo_text.send_keys(Keys.ENTER)

        geo_button = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,"button.exito-geolocation-3-x-primaryButton"))
                )
        geo_button.click()

        sleep(5)


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

        item = ExitoVinos()

        

        articulos = self.driver.find_elements_by_css_selector("div.pointer.pt3.pb4.flex.flex-column.h-100")

        for articulo in articulos:

            item["nombre"] = articulo.find_element_by_css_selector("span.vtex-store-components-3-x-productBrand").text
            

            try:
                item["precio_mililitro"]        = articulo.find_element_by_css_selector(".exito-vtex-components-4-x-mainContainerProductPum div").text[12:]
            except NoSuchElementException:
                item["precio_mililitro"]        = ""

            try:
                item["precio_sin_descuento"]    = articulo.find_element_by_css_selector("del span").text
            except NoSuchElementException:
                item["precio_sin_descuento"]    = ""
            
            try:
                item["spot_price"]              = articulo.find_element_by_css_selector(".f5.fw5 span").text
            except NoSuchElementException:
                item["spot_price"]              = ""
            
            try:
                item["porcentaje_descuento"]    = articulo.find_element_by_css_selector("div.exito-product-details-3-x-badgeExito").text
            except NoSuchElementException:
                item["porcentaje_descuento"]    = ""

            now = datetime.now()
            item["date"] = now.strftime("%m/%d/%Y %H:%M:%S")

            yield item


        self.driver.close()
