import scrapy


class Stock(scrapy.Item):
    """docstring for Stock"""
    url = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    size = scrapy.Field()