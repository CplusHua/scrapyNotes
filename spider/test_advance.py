import urllib  
import urllib2  
 
 
#User-Agent : ��Щ�������� Proxy ��ͨ����ֵ���ж��Ƿ������������������
#Content-Type : ��ʹ�� REST �ӿ�ʱ�������������ֵ������ȷ�� HTTP Body �е����ݸ�����������
#application/xml �� �� XML RPC���� RESTful/SOAP ����ʱʹ��
#application/json �� �� JSON RPC ����ʱʹ��
#application/x-www-form-urlencoded �� ������ύ Web ��ʱʹ��
#��ʹ�÷������ṩ�� RESTful �� SOAP ����ʱ�� Content-Type ���ô���ᵼ�·������ܾ�����


url = 'http://178448.com/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.37 Safari/537.36'  
#user_agent= 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'aa':'12' }  
headers = { 'User-Agent' : user_agent, 
            #'Referer':'http://178448.com',
            #'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            #'Accept-Encoding':'gzip, deflate, sdch',
            #'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
            #'Connection':'keep-alive',
            #'Cookie':'c448k_2ce1_lastcheckfeed=275345%7C1425173895; c448k_2ce1_nofavfid=1; c448k_2ce1_home_readfeed=1425706751; c448k_2ce1_home_diymode=1; pgv_info=ssid=s6197747732; pgv_pvid=7439358172; BAIDU_DUP_lcr=http://www.baidu.com/link?url=uLj5FE2ZDOymH_fj1ddTVRonu46Ww8r1wQz3Uo_-lo7&wd=%E8%82%A1%E6%B5%B7%E6%98%8E%E7%81%AF&issp=1&f=8&ie=utf-8&tn=90269354_hao_pg; c448k_2ce1_st_t=275345%7C1431747725%7C74e6fc5745b1a5136befc17577568695; c448k_2ce1_forum_lastvisit=D_128_1431747725; c448k_2ce1_saltkey=FcZG9Ijj; c448k_2ce1_lastvisit=1432037952; CNZZDATA1613261=cnzz_eid%3D1557278417-1426506812-%26ntime%3D1432037087; c448k_2ce1_con_request_uri=http%3A%2F%2Fwww.178448.com%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dforum.php%253Fmod%253Dviewthread%2526tid%253D926640%2526extra%253Dpage%25253D1%2526page%253D1; c448k_2ce1_client_created=1432041715; c448k_2ce1_client_token=882C9F528A33070AA479F60C7D5CF4CF; c448k_2ce1_ulastactivity=5010JUSWIF1pOyE1zHLIAodE1lDfeLJdCM7qx%2BvEMvaxCXl8bpqY; c448k_2ce1_auth=71557mi%2Bo7OFTgG4SqOan5MmFyiOR6oLU0Gisg8MzG55S9HcQbrhX9VXagdJO69AQUMmPhZ4zkJqWo1ip%2FrCwnLpzi4; c448k_2ce1_connect_login=1; c448k_2ce1_connect_uin=882C9F528A33070AA479F60C7D5CF4CF; c448k_2ce1_stats_qc_login=3; c448k_2ce1_security_cookiereport=3905xGert77llew6GW7rBO7RGI2TQTcerC%2BXFdcqq663%2FrljesKS; c448k_2ce1_connect_not_sync_t=1; c448k_2ce1_st_p=275345%7C1432042189%7C1a5033022c663f4f95e02575a4a1705c; c448k_2ce1_visitedfid=167D162D128D166D92D147D266D179; c448k_2ce1_viewid=tid_926746; c448k_2ce1_sid=EO9o6D; c448k_2ce1_lip=183.17.255.201%2C1432042190; c448k_2ce1_lastact=1432042190%09home.php%09spacecp; c448k_2ce1_connect_is_bind=1; Hm_lvt_aa669fe24aabb489080c05a96e7f594b=1432041592; Hm_lpvt_aa669fe24aabb489080c05a96e7f594b=1432042205; c448k_2ce1_smile=1D1'
            }  
data = urllib.urlencode(values)  
request = urllib2.Request(url, data, headers)  
try :
    response = urllib2.urlopen(request)  
except urllib2.URLError, e:
    print e.reason
    
page = response.read() 
print page

print ' done ! '


#import urllib2
#enable_proxy = True
#proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
#null_proxy_handler = urllib2.ProxyHandler({})
#if enable_proxy:
    #opener = urllib2.build_opener(proxy_handler)
#else:
    #opener = urllib2.build_opener(null_proxy_handler)
#urllib2.install_opener(opener)














import urllib2
import cookielib
#����һ��CookieJar����ʵ��������cookie
cookie = cookielib.CookieJar()
#����urllib2���HTTPCookieProcessor����������cookie������
handler=urllib2.HTTPCookieProcessor(cookie)
#ͨ��handler������opener
opener = urllib2.build_opener(handler)
#�˴���open����ͬurllib2��urlopen������Ҳ���Դ���request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value

#HTTPError��URLError�����࣬��������urlopen��������һ������ʱ���������϶����Ӧһ��Ӧ�����response������������һ�����֡�״̬�롱���ٸ����ӣ�����response��һ�����ض��򡱣��趨λ����ĵ�ַ��ȡ�ĵ���urllib2���Դ˽��д���

#�������ܴ���ģ�urlopen�����һ��HTTPError����Ӧ��Ӧ��״̬��HTTP״̬���ʾHTTPЭ�������ص���Ӧ��״̬�����潫״̬�������£�

#100������  �ͻ���Ӧ�������������󡣿ͻ���Ӧ���������������ʣ�ಿ�֣�������������Ѿ���ɣ����������Ӧ��
#101�� ת��Э��  �ڷ����������Ӧ���Ŀ��к󣬷����������л�����Upgrade ��Ϣͷ�ж������ЩЭ�顣ֻ�����л��µ�Э����кô���ʱ���Ӧ�ò�ȡ���ƴ�ʩ��
#102����������   ��WebDAV��RFC 2518����չ��״̬�룬������������ִ�С�
#200������ɹ�      ����ʽ�������Ӧ�����ݣ����д���
#201��������ɣ�����Ǵ���������Դ���´�����Դ��URI������Ӧ��ʵ���еõ�    ����ʽ�������в�������
#202�����󱻽��ܣ���������δ���    ����ʽ�������ȴ�
#204�����������Ѿ�ʵ�������󣬵���û�з����µ��� Ϣ������ͻ����û�����������Ϊ�˸���������ĵ���ͼ��    ����ʽ������
#300����״̬�벻��HTTP/1.0��Ӧ�ó���ֱ��ʹ�ã� ֻ����Ϊ3XX���ͻ�Ӧ��Ĭ�Ͻ��͡����ڶ�����õı�������Դ��    ����ʽ�����������ܹ���������н�һ��������������в��ܴ�������
#301�����󵽵���Դ�������һ�����õ�URL�������Ϳ����ڽ���ͨ����URL�����ʴ���Դ    ����ʽ���ض��򵽷����URL
#302�����󵽵���Դ��һ����ͬ��URL����ʱ����     ����ʽ���ض�����ʱ��URL
#304���������Դδ����     ����ʽ������
#400���Ƿ�����     ����ʽ������
#401��δ��Ȩ     ����ʽ������
#403����ֹ     ����ʽ������
#404��û���ҵ�     ����ʽ������
#500���������ڲ�����  ������������һ��δ��Ԥ�ϵ�״�������������޷���ɶ�����Ĵ���һ����˵��������ⶼ���ڷ������˵�Դ������ִ���ʱ���֡�
#501���������޷�ʶ��  ��������֧�ֵ�ǰ��������Ҫ��ĳ�����ܡ����������޷�ʶ������ķ����������޷�֧������κ���Դ������
#502����������  ��Ϊ���ػ��ߴ������ķ���������ִ������ʱ�������η��������յ���Ч����Ӧ��
#503���������   ������ʱ�ķ�����ά�����߹��أ���������ǰ�޷������������״������ʱ�ģ����ҽ���һ��ʱ���Ժ�ָ���