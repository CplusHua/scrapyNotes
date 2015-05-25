# -*-coding:utf-8 -*-
# author : zhuyb
#
# -- file : secondNewStock.py

import requests
import gzip
import StringIO
import ConfigParser
import sys
from bs4 import BeautifulSoup
import time
import re
# import MySQLdb 
import urllib2
import urllib
import cookielib


# #######################################################################
class SecondNewStock:
    """ 从网上爬取最近开板的次新股 """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.siteurl="http://quote.cfi.cn/"
        self.reStockpattern = re.compile(r'\d{6}')
        cf = ConfigParser.ConfigParser()
        cf.read("config.ini")
    
        self.pageCount = int( cf.get("spider","pageCount") )
        # host = cf.get("db","host")
        # port = int(cf.get("db","port"))
        # user = cf.get("db","user")
        # passwd = cf.get("db","passwd")
        # db_name = cf.get("db","db")
        # charset = cf.get("db","charset")
        # use_unicode = cf.get("db","use_unicode")
    
        # self.db = MySQLdb.connect(host=host, port=port, user=user,\
                                  # passwd=passwd, db=db_name, \
                                  # charset=charset,use_unicode=use_unicode)
        # self.cursor = self.db.cursor() 
        #代理IP地址，防止自己的IP被封禁
        self.proxyURL = 'http://192.168.204.157:8000'        
        #设置代理
        self.proxy = urllib2.ProxyHandler({'http':self.proxyURL})
        #设置cookie
        self.cookie = cookielib.LWPCookieJar()
        #设置cookie处理器
        self.cookieHandler = urllib2.HTTPCookieProcessor(self.cookie)
        #设置登录时用到的opener，它的open方法相当于urllib2.urlopen
        self.opener = urllib2.build_opener(self.cookieHandler,self.proxy,urllib2.HTTPHandler)        
        
        print 'inti done!'
        
    #获取索引页面的内容
    # http://quote.cfi.cn/drawchartany.aspx?nodeid=223&pageindex=4&jdfwkey=j7rb6
    def getPage(self,pageIndex):
        url = self.siteurl + 'drawchartany.aspx?nodeid=223&jdfwkey=j7rb6&pageindex='+str(pageIndex)
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.37 Safari/537.36'  
        #user_agent= 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        values = {  }  
        headers = { 'User-Agent' : user_agent, 
                    'Referer':'http://newstock.cfi.cn/',
                    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Encoding':'gzip, deflate, sdch',
                    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6'
                    #'Connection':'keep-alive',
                    #'Cookie':'c448k_2ce1_lastcheckfeed=275345%7C1425173895; c448k_2ce1_nofavfid=1; c448k_2ce1_home_readfeed=1425706751; c448k_2ce1_home_diymode=1; pgv_info=ssid=s6197747732; pgv_pvid=7439358172; BAIDU_DUP_lcr=http://www.baidu.com/link?url=uLj5FE2ZDOymH_fj1ddTVRonu46Ww8r1wQz3Uo_-lo7&wd=%E8%82%A1%E6%B5%B7%E6%98%8E%E7%81%AF&issp=1&f=8&ie=utf-8&tn=90269354_hao_pg; c448k_2ce1_st_t=275345%7C1431747725%7C74e6fc5745b1a5136befc17577568695; c448k_2ce1_forum_lastvisit=D_128_1431747725; c448k_2ce1_saltkey=FcZG9Ijj; c448k_2ce1_lastvisit=1432037952; CNZZDATA1613261=cnzz_eid%3D1557278417-1426506812-%26ntime%3D1432037087; c448k_2ce1_con_request_uri=http%3A%2F%2Fwww.178448.com%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dforum.php%253Fmod%253Dviewthread%2526tid%253D926640%2526extra%253Dpage%25253D1%2526page%253D1; c448k_2ce1_client_created=1432041715; c448k_2ce1_client_token=882C9F528A33070AA479F60C7D5CF4CF; c448k_2ce1_ulastactivity=5010JUSWIF1pOyE1zHLIAodE1lDfeLJdCM7qx%2BvEMvaxCXl8bpqY; c448k_2ce1_auth=71557mi%2Bo7OFTgG4SqOan5MmFyiOR6oLU0Gisg8MzG55S9HcQbrhX9VXagdJO69AQUMmPhZ4zkJqWo1ip%2FrCwnLpzi4; c448k_2ce1_connect_login=1; c448k_2ce1_connect_uin=882C9F528A33070AA479F60C7D5CF4CF; c448k_2ce1_stats_qc_login=3; c448k_2ce1_security_cookiereport=3905xGert77llew6GW7rBO7RGI2TQTcerC%2BXFdcqq663%2FrljesKS; c448k_2ce1_connect_not_sync_t=1; c448k_2ce1_st_p=275345%7C1432042189%7C1a5033022c663f4f95e02575a4a1705c; c448k_2ce1_visitedfid=167D162D128D166D92D147D266D179; c448k_2ce1_viewid=tid_926746; c448k_2ce1_sid=EO9o6D; c448k_2ce1_lip=183.17.255.201%2C1432042190; c448k_2ce1_lastact=1432042190%09home.php%09spacecp; c448k_2ce1_connect_is_bind=1; Hm_lvt_aa669fe24aabb489080c05a96e7f594b=1432041592; Hm_lpvt_aa669fe24aabb489080c05a96e7f594b=1432042205; c448k_2ce1_smile=1D1'
                    }  
        data = urllib.urlencode(values)  
        print url
        request = urllib2.Request(url, data, headers)  
        try :
            response = urllib2.urlopen(request) 
            #response = self.opener.open(url)
        except urllib2.URLError, e:
            print e.reason   
        page = response.read()
        page = page[54:-1] 
        return page[0:-19]   
    
    #----------------------------------------------------------------------
    def parseTable(self,page):
        """"""
        soup = BeautifulSoup( page)
        trs = soup.table.find_all('tr')
        isFirst=0
        table = []
        for tr in trs[0:-1]:
            #tds = tr.find_all('td')
            row =[]                        
            #print type(td.get_text()) unicode
            #row.append(td.get_text())
            row = self.parseRowTd(tr, isFirst)
            isFirst = isFirst+1
                
            table.append(row)
        return table[1:len(table)]
        #print trs[0].prettify()
     
    #----------------------------------------------------------------------
    def parseRowTd(self,tr,isFirst=0):
        """"""
        row = []
        colno = 0
        stockcode =''
        for td in tr.find_all('td'):
            if isFirst == 0 :
                row.append(td.get_text())
            else:
                if colno == 0:
                    href = td.a['href']                     
                    row.append(td.a.get_text())
                elif colno == 1 :
                    row.append(td.get_text())
                elif colno == 2 :
                    span =td.find_all('span')[0]
                    row.append(span.get_text())                
                else :
                    row.append(td.get_text())            
                   
            colno += 1
        if isFirst > 0 and len(href) > 15 :
            # stockcode = re.match(self.reStockpattern, href)
            stockcode = href[-11:-5]
            #print stockcode 
            #print href
            row.append(stockcode)
            row.append(href)
        else:
            row.append('')
            row.append('')
        #print type(row[0]) # unicode
        #print(row[0])      # 汉子
        #print ','.join(row)
        return row
        
    #----------------------------------------------------------------------
    # def insertOne(self,val):
        # """"""
        # value =[]
        # print len(val)
        # for s in val :
            # value.append(s.encode('utf8').strip())         
        # print value
        # #sql = "insert into SecondNewStock(`NAME`,`FXJ`,`ZTS`,`QGSY`,`QGCB`,`ZJSYL`,`FXL`,`FXSY`,`ZQL`,`SSR`,`PBR`,`PBZJ`,`PBZF`,`ZXJ`,`CODE`,`URL`) values('田中精机' ,'7.92' ,'4' ,'7250元(浮盈)' ,'641万' ,'0.11%(浮盈)' ,'3268万' ,'22.98倍' ,         '0.124%'  ,'20150519' ,'--' ,'--' ,'--' ,'15.17',      '300461','http://quote.cfi.cn/quote_300461.html ')"
        # sql = "insert into SecondNewStock(`NAME`,`FXJ`,`ZTS`,`QGSY`,`QGCB`,`ZJSYL`,`FXL`,`FXSY`,`ZQL`,`SSR`,`PBR`,`PBZJ`,`PBZF`,`ZXJ`,`CODE`,`URL`)\
        # values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # #'田中精机' ,'7.92' ,'4' ,'7250元(浮盈)' ,'641万' ,'0.11%(浮盈)' ,'3268万' ,'22.98倍' ,      \
        # #'0.124%'  ,'20150519' ,'--' ,'--' ,'--' ,'15.17',      '300461','http://quote.cfi.cn/quote_300461.html ')"
        # r = self.cursor.execute(sql,value)
        # print 'Done ! sql excuted  %s rows ' % r 
            
    #----------------------------------------------------------------------
    def genSql(self,val):
        """"""
        value =[]
        #print len(val)
        for s in val :
            value.append(s.encode('gbk').strip())         
        #print value
        #sql = "insert into SecondNewStock(`NAME`,`FXJ`,`ZTS`,`QGSY`,`QGCB`,`ZJSYL`,`FXL`,`FXSY`,`ZQL`,`SSR`,`PBR`,`PBZJ`,`PBZF`,`ZXJ`,`CODE`,`URL`) values('田中精机' ,'7.92' ,'4' ,'7250元(浮盈)' ,'641万' ,'0.11%(浮盈)' ,'3268万' ,'22.98倍' ,         '0.124%'  ,'20150519' ,'--' ,'--' ,'--' ,'15.17',      '300461','http://quote.cfi.cn/quote_300461.html ')"
        sql = "insert into SecondNewStock(`NAME`,`FXJ`,`ZTS`,`QGSY`,`QGCB`,`ZJSYL`,`FXL`,`FXSY`,`ZQL`,`SSR`,`PBR`,`PBZJ`,`PBZF`,`ZXJ`,`CODE`,`URL`)\
        values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        sql = sql % tuple(value )
        return sql
        #'田中精机' ,'7.92' ,'4' ,'7250元(浮盈)' ,'641万' ,'0.11%(浮盈)' ,'3268万' ,'22.98倍' ,      \
        #'0.124%'  ,'20150519' ,'--' ,'--' ,'--' ,'15.17',      '300461','http://quote.cfi.cn/quote_300461.html ')"
        #r = self.cursor.execute(sql,value)
        #print 'Done ! sql excuted  %s rows ' % r                       

    #----------------------------------------------------------------------
    def run(self):
        """"""
        n = self.pageCount 
        toltal = range(n)
        page = ''
        tables = []
        
        table= []
        
        for i in toltal:
            page = self.getPage(i+1)
            #Wprint page
            table = self.parseTable(page)
            tables += table 
         #print  len(table)  
        #self.insertOne(tables[1])
        #self.genSql(tables[1])
        file_object = open('newstock.txt','w+')
        file_sql = open('newstock.sql','w+')
        try:
            lines = []
            sqls = []
            for line in tables:
                l =''
                sqls.append(self.genSql(line)+';\n')
                for it in line:
                    it = it.encode('gbk')
                    #print it
                    l = "%s ,%s" % (l  ,  it.strip() )
                l = "%s \n" % l.strip(' ,')    
                lines.append(l)
            print len(sqls)
            all_the_text = file_sql.writelines(sqls)
            all_the_text = file_object.writelines(lines)
        finally:
            file_object.close( )
            file_sql.close()
        
        
        
    
def main():
    app = SecondNewStock()
    app.run()
    
if __name__ == '__main__':
        main()
        print 'Done !'