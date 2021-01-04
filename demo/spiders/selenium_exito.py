import scrapy
import random

from scrapy_selenium import SeleniumRequest

from ..items import ExitoSeleniumItem





class SeleniumExitoSpider(scrapy.Spider):
    name = 'selenium_exito'
    allowed_domains = ['exito.com']
    # start_urls = ['http://exito.com/']

    def start_requests(self):
        # yield SeleniumRequest(url="https://www.exito.com/tecnologia/televisores?page=2", callback = self.parse)
        yield SeleniumRequest(url="https://www.exito.com/tecnologia/televisores", callback = self.parse)




    def parse(self, response):


        item            = ExitoSeleniumItem()

        articulos       = response.css("article.vtex-product-summary-2-x-element.pointer.pt3.pb4.flex.flex-column.h-100")
        articulos       = articulos.css("div.pointer.pt3.pb4.flex.flex-column.h-100")
        

        for articulo in articulos:

            item["nombre"]                 = articulo.css("span.vtex-store-components-3-x-productBrand::text").get()
            item["precio_sin_descuento"]   = articulo.css(".search-result-exito-vtex-components-list-price span::text").get()
            item["precio_aliados"]         = articulo.css(".search-result-exito-vtex-components-allies-discount span::text").get()
            item["spot_price"]             = articulo.css(".search-result-exito-vtex-components-selling-price span::text").get()


            yield item


        

        
