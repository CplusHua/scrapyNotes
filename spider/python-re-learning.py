# -*- coding: utf-8 -*-
#返回pattern对象
#re.compile(string[,flag])  
##以下为匹配所用函数
#re.match(pattern, string[, flags])
#re.search(pattern, string[, flags])
#re.split(pattern, string[, maxsplit])
#re.findall(pattern, string[, flags])
#re.finditer(pattern, string[, flags])
#re.sub(pattern, repl, string[, count])
#re.subn(pattern, repl, string[, count])


### re.I(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
### re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
### re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
### re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
### re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
### re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。


__author__ = 'CQC'
# -*- coding: utf-8 -*-

#导入re模块
import re

# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'hello')

# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.match(pattern,'hello')
result2 = re.match(pattern,'helloo CQC!')
result3 = re.match(pattern,'helo CQC!')
result4 = re.match(pattern,'hello CQC!')

#如果1匹配成功
if result1:
    # 使用Match获得分组信息
    print result1.group()
else:
    print '1匹配失败！'


#如果2匹配成功
if result2:
    # 使用Match获得分组信息
    print result2.group()
else:
    print '2匹配失败！'


#如果3匹配成功
if result3:
    # 使用Match获得分组信息
    print result3.group()
else:
    msg ='3匹配失败！'
    print type(msg)
    msg = msg.decode('utf-8')
    print msg

#如果4匹配成功
if result4:
    # 使用Match获得分组信息
    print result4.group()
else:
    print '4匹配失败！'
    
    
    
    
    #1.string: 匹配时使用的文本。
    #2.re: 匹配时使用的Pattern对象。
    #3.pos: 文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
    #4.endpos: 文本中正则表达式结束搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
    #5.lastindex: 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
    #6.lastgroup: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。
    #方法：
    #1.group([group1, …]):
    #获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
    #2.groups([default]):
    #以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。
    #3.groupdict([default]):
    #返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。
    #4.start([group]):
    #返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
    #5.end([group]):
    #返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
    #6.span([group]):
    #返回(start(group), end(group))。
    #7.expand(template):
    #将匹配到的分组代入template中然后返回。template中可以使用\id或\g、\g引用分组，但不能使用编号0。\id与\g是等价的；但\10将被认为是第10个分组，如果你想表达\1之后是字符’0’，只能使用\g0。
    
    
    # -*- coding: utf-8 -*-
    #一个简单的match实例
    
    import re
    # 匹配如下内容：单词+空格+单词+任意字符
    m = re.match(r'(\w+) (\w+)(?P.*)', 'hello world!')
    
    print "m.string:", m.string
    print "m.re:", m.re
    print "m.pos:", m.pos
    print "m.endpos:", m.endpos
    print "m.lastindex:", m.lastindex
    print "m.lastgroup:", m.lastgroup
    print "m.group():", m.group()
    print "m.group(1,2):", m.group(1, 2)
    print "m.groups():", m.groups()
    print "m.groupdict():", m.groupdict()
    print "m.start(2):", m.start(2)
    print "m.end(2):", m.end(2)
    print "m.span(2):", m.span(2)
    print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')
    
    ### output ###
    # m.string: hello world!
    # m.re: 
    # m.pos: 0
    # m.endpos: 12
    # m.lastindex: 3
    # m.lastgroup: sign
    # m.group(1,2): ('hello', 'world')
    # m.groups(): ('hello', 'world', '!')
    # m.groupdict(): {'sign': '!'}
    # m.start(2): 6
    # m.end(2): 11
    # m.span(2): (6, 11)
    # m.expand(r'\2 \1\3'): world hello!    
    
    
    #导入re模块
    import re
    
    # 将正则表达式编译成Pattern对象
    pattern = re.compile(r'world')
    # 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
    # 这个例子中使用match()无法成功匹配
    match = re.search(pattern,'hello world!')
    if match:
        # 使用Match获得分组信息
        print match.group()
    ### 输出 ###
    # world    
    
    
    
    
    #match(string[, pos[, endpos]]) | re.match(pattern, string[, flags])
    #search(string[, pos[, endpos]]) | re.search(pattern, string[, flags])
    #split(string[, maxsplit]) | re.split(pattern, string[, maxsplit])
    #findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags])
    #finditer(string[, pos[, endpos]]) | re.finditer(pattern, string[, flags])
    #sub(repl, string[, count]) | re.sub(pattern, repl, string[, count])
    #subn(repl, string[, count]) |re.sub(pattern, repl, string[, count])    