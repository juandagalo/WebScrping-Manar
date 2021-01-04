import scrapy
import json
import re
import requests

from extract import json_extract_object
from extract import json_extract_value
from ..items import ExitoUrlItem
from ..items import ExitoProductItem
from datetime import datetime

import pandas as pd

class ExitoSpider(scrapy.Spider):
    name = "exito"
    allowed_domains = ['exito.com']
    start_urls = [
        'https://www.exito.com/',
    ]

    visited_pages = []

    def findObject(self, response, pattern):

        for scripts in response.css('script'):
            if scripts.re_first(pattern) is not None:
                return scripts.re_first(pattern)
        
        return None


    def parse(self, response, base_url = "https://www.exito.com"):

        pattern = r'\b__RUNTIME__\s*=\s*(\{([^\n]*))'

        scraped_objects = self.findObject(response, pattern)

        if scraped_objects is not None:

            scraped_objects = json.loads(scraped_objects)

            urls = json_extract_value(scraped_objects, 'url')


            for url in urls:
                
                if url is not None and url != "" and url.find('?') < 0 and url.find('https://') and url.find('http://') < 0 and len(url) > 1:

                    yield scrapy.Request(f'{base_url}{url}', callback=self.parse_page, cb_kwargs=dict(url=url))





    def parse_page(self, response, url):

        items = ExitoProductItem()

        pattern = r'\b__STATE__\s*=\s*(\{([^\n]*))'

        scraped_objects_raw = self.findObject(response, pattern)

        if scraped_objects_raw is not None:

            scraped_objects = json.loads(scraped_objects_raw)

            cache_ids       = json_extract_value(scraped_objects, 'cacheId')

            cache_pattern   = re.compile(r"([^0-9])\w+")

            for cache_id in cache_ids:
                
                if cache_pattern.match(cache_id):

                    object_general_product_info     = json_extract_object(scraped_objects, f'Product:{cache_id}'.rstrip())

                    producto                        = json_extract_value(object_general_product_info,"productName")
                    categorias_objeto               = json_extract_object(object_general_product_info,"categories")
                    categorias_value                = json_extract_object(categorias_objeto,"json")

                    items['product']                = producto if len(producto) > 0 else ""
                    items['categories']             = categorias_value[0] if len(categorias_value) > 0 else ""


                    object_product_price            = json_extract_object(scraped_objects, "$Product:%s.items({%s}).0.sellers.0.commertialOffer" % (cache_id, '"filter":"ALL_AVAILABLE"'))

                    spot_price                      = json_extract_value(object_product_price,'spotPrice')
                    price_without_discount          = json_extract_value(object_product_price,'PriceWithoutDiscount')
                    list_price                      = json_extract_value(object_product_price,'ListPrice')
                    available_quantity              = json_extract_value(object_product_price,'AvailableQuantity')
                    price_valid_until               = json_extract_value(object_product_price,'PriceValidUntil')

                    items['spot_price']             = spot_price.pop() if len(spot_price) > 0 else ""
                    items['price_without_discount'] = price_without_discount.pop() if len(price_without_discount) > 0 else ""
                    items['list_price']             = list_price.pop() if len(list_price) > 0 else ""
                    items['available_quantity']     = available_quantity.pop() if len(available_quantity) > 0 else ""
                    items['price_valid_until']      = price_valid_until.pop() if len(price_valid_until) > 0 else ""


                    items['scrap_date']              = datetime.now()

                    yield items


        


            
