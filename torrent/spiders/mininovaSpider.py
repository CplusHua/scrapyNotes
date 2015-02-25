#scrapy crawl mininova -o scraped_data.json
#用上面的命令即可运行该爬虫

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from torrent.items import TorrentItem

class MininovaSpider(CrawlSpider):
    """docstring for MininovaSpider"""
    name = 'mininova'
    allowed_domains = ['mininova.org']
    start_urls  = ['http://www.mininova.org/today']
    rules = [Rule(LinkExtractor(allow=['/tor/\d+']),'parse_torrent')]

    def parse_torrent(self,response):
        torrent  = TorrentItem()
        torrent['url'] = response.url
        torrent['name'] = response.xpath("//h1/text()").extract()
        torrent['description'] = response.xpath("//div[@id='description']").extract()
        torrent['size'] = response.xpath("//div[@id='info-left']/p[2]/text()[2]").extract()
        return torrent
 
   # def __init__(self, arg):
   #     super(MininovaSpider, self).__init__()
   #     self.arg = arg

##############################################################
## 该爬虫需要的目录结构
## │  note.txt
## │  scraped_data.json
## │  scrapy.cfg
## │
## └─torrent
##     │  items.py
##     │  items.pyc
##     │  pipelines.py
##     │  settings.py
##     │  settings.pyc
##     │  __init__.py
##     │  __init__.pyc
##     │
##     └─spiders
##             mininovaSpider.py
##             mininovaSpider.pyc
##             __init__.py
##             __init__.pyc