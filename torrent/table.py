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
from torrent.row import TableRow

class TableFjzt( ):
    """docstring for Table"""
    def __init__(self,table):
    	self.table = table
        soup = BeautifulSoup(self.table)
        trs = soup.findAll('tr')
        data=[]
        for tr in trs :
        	tableRow = TableRow(tr)
        	rowOne = tableRow.parseTableOfRow(tr)
        	data.append(rowOne)
        print data

    def parseTable(table):
    	soup = BeautifulSoup( table)
        trs = soup.findAll('tr')
        data=[]
        for tr in trs :
        	 tableRow = TableRow(tr)
        	 #print tr
        	 rowOne = tableRow.parseTableOfRow(tr.encode('utf-8'))
        	 data.append(rowOne)
        return data
    	
if __name__ == '__main__':
    trow = TableFjzt("")