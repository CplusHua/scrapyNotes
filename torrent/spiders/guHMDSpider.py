# -*-coding:utf-8-*-
# set PATH=D:\Program Files\python27-64\Scripts;%PATH%
#scrapy crawl ghmd -o scraped_data.json
#用上面的命令即可运行该爬虫
import MySQLdb
from bs4 import BeautifulSoup
import json
import re
import time
from math import ceil
import logging
import threading
import Queue
import ConfigParser
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from torrent.stocks import Stock
from torrent.row import TableRow
from torrent.table import TableFjzt
 

class GhmdStockSpider(CrawlSpider):
    """docstring for GhmdStockSpider"""
    name = 'ghmd'
    allowed_domains = ['178448.com']
    start_urls  = ['http://178448.com/fjzt-1.html']
    rules = [Rule(LinkExtractor(allow=['/fjzt-1.html']),'parse_stock')]
    #self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    #self.headers = { 'User-Agent' : self.user_agent }

    def parse_stockXpath(self,response):
        pageOne  = Stock()
        pageOne['url'] = response.url
        #<div class="datalist">
        pageOne['name'] = response.xpath("//title/text()").extract()
        #pageOne['ct'] = response.xpath("//div[@id='ct']").extract()
        #pageOne['div1'] = response.xpath("//div[@id='ct']/div[1]/div[4]").extract()
        pageOne['tableHeadrow'] = response.xpath("//div[@class='datalist']/table/thead/tr").extract()
        pageOne['tableBodyrowlist'] = response.xpath("//div[@class='datalist']/table/tbody/tr").extract()
        print '------------------------------------------------------------------------------'
        print pageOne
        return pageOne

    def parse_stock(self,response):
        pageOne  = Stock()
        pageOne['url'] = response.url
        #<div class="datalist">
        pageOne['name'] = response.xpath("//title/text()").extract()
        #pageOne['ct'] = response.xpath("//div[@id='ct']").extract()
        #pageOne['div1'] = response.xpath("//div[@id='ct']/div[1]/div[4]").extract()
        pageOne['datalist'] = response.xpath("//div[@class='datalist']/table").extract()
        #soup = BeautifulSoup(response.xpath("/body").extract())
        #divlist = soup.find_all('div',class_='datalist')
        #if(len(divlist ) > 0):
        #    tableSoup = divlist[0].find('table')
        #    print tableSoup         
        print len(pageOne['datalist'])
        if(len(pageOne['datalist']) > 0):
            jsonDataTable = TableFjzt(pageOne['datalist'][0])
            jsonData = jsonDataTable.parseTable(pageOne['datalist'][0])
            print '------------------------------------------------------------------------------'
            return jsonData
        else:
            return []
    #def __init__(self, arg):
    #    super(THSStockSpider, self).__init__()
    #    self.arg = arg
