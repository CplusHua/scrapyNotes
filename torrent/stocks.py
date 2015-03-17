import scrapy


class Stock(scrapy.Item):
    """docstring for Stock"""
    url = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    size = scrapy.Field()
    datalist = scrapy.Field()
    tableBodyrowlist = scrapy.Field()
    tableHeadrow = scrapy.Field()
    tabledatalist = scrapy.Field()