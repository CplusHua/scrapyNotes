 
import urllib2

response = urllib2.urlopen("http://www.baidu.com")
print response.read()

#�������ǵ��õ���urllib2�������urlopen����������һ��URL�������ַ�ǰٶ���ҳ��Э����HTTPЭ�飬��Ȼ��Ҳ���԰�HTTP����FTP,FILE,HTTPS �ȵȣ�ֻ�Ǵ�����һ�ַ��ʿ���Э�飬urlopenһ������������������Ĳ������£�
#
#
# urlopen(url, data, timeout)
#��һ������url��ΪURL���ڶ�������data�Ƿ���URLʱҪ���͵����ݣ�������timeout�����ó�ʱʱ�䡣
#
# �ڶ����������ǿ��Բ����͵ģ�dataĬ��Ϊ��None��timeoutĬ��Ϊ socket._GLOBAL_DEFAULT_TIMEOUT
#
# ��һ������URL�Ǳ���Ҫ���͵ģ�����������������Ǵ����˰ٶȵ�URL��ִ��urlopen����֮�󣬷���һ��response���󣬷�����Ϣ�㱣���������档
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