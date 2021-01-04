# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExitoUrlItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()

class ExitoProductItem(scrapy.Item):
    # define the fields for your item here like:
    product = scrapy.Field()
    categories = scrapy.Field()

    # selling_price_high= scrapy.Field()
    # selling_price_low= scrapy.Field()

    # list_price_high = scrapy.Field()
    # list_price_low = scrapy.Field()

    spot_price = scrapy.Field()
    price_without_discount = scrapy.Field()
    list_price = scrapy.Field()

    available_quantity = scrapy.Field()

    price_valid_until = scrapy.Field()

    scrap_date = scrapy.Field()

    # title = scrapy.Field()


class ExitoSeleniumItem(scrapy.Item):
    # define the fields for your item here like:
    nombre                  = scrapy.Field()
    precio_sin_descuento    = scrapy.Field()
    precio_aliados          = scrapy.Field()
    spot_price              = scrapy.Field()
    date                    = scrapy.Field()


class ExitoVinos(scrapy.Item):
    # define the fields for your item here like:
    nombre                  = scrapy.Field()
    precio_mililitro        = scrapy.Field()
    precio_sin_descuento    = scrapy.Field()
    spot_price              = scrapy.Field()
    porcentaje_descuento    = scrapy.Field()

