import scrapy
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


class TableRow( ):
    """docstring for Stock"""
    def __init__(self,row):
    	self.row = row.encode('utf-8')
    	soup = BeautifulSoup(self.row)
        tds = soup.findAll('td')
        data=[]
        for td in tds :
        	if(len(data) == 0):
        		uid = td.findAll('a')
        		href = ''
        		if len(uid)==0 :
        			data.append(href)
        			data.append(href)
        		else:
	        		if uid[0].has_attr('href'):
	        			href = uid[0].attrs['href']
	        		data.append(href)
	        		nameUser = uid[0].text
	        		data.append(nameUser)
        	else:
        		value = td.text
        		data.append(value)
        #print data

    def parseTableOfRow(row):
     	soup = BeautifulSoup(row)
        tds = soup.findAll('td')
        data=[]
        for td in tds :
        	if(len(data) == 0):
        		uid = td.findAll('a')
        		href = ''
        		if len(uid)==0 :
        			data.append(href)
        			data.append(href)
        		else:
	        		if uid[0].has_attr('href'):
	        			href = uid[0].attrs['href']
	        		data.append(href)
	        		nameUser = uid[0].text
	        		data.append(nameUser)
        	else:
        		value = td.text
        		data.append(value)
        #print data
        return data

if __name__ == '__main__':
    trow = TableRow("<tr><td><a href=\"fjzt-6.html?uid=236625\"> \u6728\u6613\u541b</a></td>\r\n<td class=\"bzt\">71.5</td>\r\n<td>26.78%</td>\r\n    <td>\u5efa\u65b0\u77ff\u4e1a</td>\r\n<td>000688</td>\r\n<td>2015-03-17  10:27</td>\r\n<td>8.61</td>\r\n<td class=\"tdb\"><span id=\"s775741\"></span></td>\r\n<td class=\"tdb\"><span id=\"zf775741\"></span></td>\r\n<td class=\"bzt\">--</td><td></td>\r\n</tr>")