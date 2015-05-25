import urllib  
import urllib2  
 
 
#User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
#Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
#application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
#application/json ： 在 JSON RPC 调用时使用
#application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
#在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务


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
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value

#HTTPError是URLError的子类，在你利用urlopen方法发出一个请求时，服务器上都会对应一个应答对象response，其中它包含一个数字”状态码”。举个例子，假如response是一个”重定向”，需定位到别的地址获取文档，urllib2将对此进行处理。

#其他不能处理的，urlopen会产生一个HTTPError，对应相应的状态吗，HTTP状态码表示HTTP协议所返回的响应的状态。下面将状态码归结如下：

#100：继续  客户端应当继续发送请求。客户端应当继续发送请求的剩余部分，或者如果请求已经完成，忽略这个响应。
#101： 转换协议  在发送完这个响应最后的空行后，服务器将会切换到在Upgrade 消息头中定义的那些协议。只有在切换新的协议更有好处的时候才应该采取类似措施。
#102：继续处理   由WebDAV（RFC 2518）扩展的状态码，代表处理将被继续执行。
#200：请求成功      处理方式：获得响应的内容，进行处理
#201：请求完成，结果是创建了新资源。新创建资源的URI可在响应的实体中得到    处理方式：爬虫中不会遇到
#202：请求被接受，但处理尚未完成    处理方式：阻塞等待
#204：服务器端已经实现了请求，但是没有返回新的信 息。如果客户是用户代理，则无须为此更新自身的文档视图。    处理方式：丢弃
#300：该状态码不被HTTP/1.0的应用程序直接使用， 只是作为3XX类型回应的默认解释。存在多个可用的被请求资源。    处理方式：若程序中能够处理，则进行进一步处理，如果程序中不能处理，则丢弃
#301：请求到的资源都会分配一个永久的URL，这样就可以在将来通过该URL来访问此资源    处理方式：重定向到分配的URL
#302：请求到的资源在一个不同的URL处临时保存     处理方式：重定向到临时的URL
#304：请求的资源未更新     处理方式：丢弃
#400：非法请求     处理方式：丢弃
#401：未授权     处理方式：丢弃
#403：禁止     处理方式：丢弃
#404：没有找到     处理方式：丢弃
#500：服务器内部错误  服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。一般来说，这个问题都会在服务器端的源代码出现错误时出现。
#501：服务器无法识别  服务器不支持当前请求所需要的某个功能。当服务器无法识别请求的方法，并且无法支持其对任何资源的请求。
#502：错误网关  作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。
#503：服务出错   由于临时的服务器维护或者过载，服务器当前无法处理请求。这个状况是临时的，并且将在一段时间以后恢复。