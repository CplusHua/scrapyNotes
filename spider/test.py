 
import urllib2

response = urllib2.urlopen("http://www.baidu.com")
print response.read()

#首先我们调用的是urllib2库里面的urlopen方法，传入一个URL，这个网址是百度首页，协议是HTTP协议，当然你也可以把HTTP换做FTP,FILE,HTTPS 等等，只是代表了一种访问控制协议，urlopen一般接受三个参数，它的参数如下：
#
#
# urlopen(url, data, timeout)
#第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。
#
# 第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT
#
# 第一个参数URL是必须要传送的，在这个例子里面我们传送了百度的URL，执行urlopen方法之后，返回一个response对象，返回信息便保存在这里面。
#
request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()



# ####################post
import urllib
#import urllib2

values = {"username":"1016903103@qq.com","password":"XXXX"}
data = urllib.urlencode(values) 
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()


#  
import urllib
import urllib2

values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = urllib.urlencode(values) 
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()