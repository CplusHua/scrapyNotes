# -*-coding:utf-8-*-
#scrapy crawl xueqiu -o scraped_data.json
#用上面的命令即可运行该爬虫

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from torrent.stocks import Stock

class XQStockSpider(CrawlSpider):
    """docstring for XQStockSpider"""
    name = 'xueqiu'
    allowed_domains = ['xueqiu.com']
    start_urls  = ['http://xueqiu.com/S/SZ000498']
    rules = [Rule(LinkExtractor(allow=['/S/\d+']),'parse_stock')]

    def parse_stock():
        torrent  = Stock()
        torrent['url'] = response.url
        torrent['name'] = response.xpath("//h1/text()").extract()
        torrent['description'] = response.xpath("//div[@id='description']").extract()
        torrent['size'] = response.xpath("//div[@id='info-left']/p[2]/text()[2]").extract()
        return torrent

    #def __init__(self, arg):
    #    super(THSStockSpider, self).__init__()
    #    self.arg = arg
