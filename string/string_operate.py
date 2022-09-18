'''

字符串的驻留机制
·驻留机制的几种情况(交互模式)
·字符串的长度为0或1时
·符合标识符的字符串
·字符串只在编译时进行驻留,而非运行时
·[-5,256]之间的整数数字
'''

'''—————————————字符串的常用操作——————————'''
'''
大小写转换

upper()把字符串中所有字符都转成大写字母
lower()把字符串中所有字符都转成小写字母
swapcase()把字符串中所有大写字母转成小写字母,把所有小写字母都转成大写字母
capitalize()把第一个字符转换为大写,把其余字符转换为小写
title()把每个单词的第一个字符转换为大写,把每个单词的剩余字符转换为小写


'''

s = 'hello,world'

a = s.upper()  # 全部变大写
print(a, id(a), id(s))  # 会产生新的地址

s1 = 'HELLO WORLD'
b = s1.lower()  # 全部变小写
print(b)  # 会产生新的地址

s2 = 'Hello,Python'  # 大小写会转化
print(s2.swapcase())

'''—————————————字符串内容对齐操作的方法——————————'''
'''center()居中对齐 1 第一个参数为指定宽度 2 第二个参数为填充符 默认为空格'''
print(s2.center(20, '-'))  # 20-12=8  分配每边为4

# ljust()左对齐
print(s.ljust(20, ))  # 若小于12则原字符

# rjust()右对齐
print(s.rjust(20, ))

# zfill()右对齐   用0来填充
print(s.zfill(20, ))

'''—————————————字符串的劈分——————————'''
# split()左边劈 默认空格 返回值是函数
s3 = 'hello world Python'
lst = s3.split()
print(lst)
print(s3.split())
# 用sep参数 指定劈分字符串
s4 = 'hello|world|Python'
print(s4.split(sep='|'))
# maxsplit指定劈分次数，剩余的字符串的单独做一部分
print(s4.split(sep='|', maxsplit=1))

# rsplit（）  R=right 从右侧劈分 其余同
print(s4.rsplit(sep='|', maxsplit=1))  # 区分点

# 如果无指定则一模一样 指定了就分左右


'''—————————————判断字符串——————————'''#判断密码是否符合
'''
___.isidentifier()判断指定的字符串是不是合法的标识符


___.isspace()判断指定的字符串是否全部由空白字符组成（回车、换行，水平制表符）

___.isalpha()判断指定的字符串是否全部由字母组成

___.isdecimal()判断指定字符串是否全部由十进制的数字组成

___.isnumeric()判断指定的字符串是否全部由数字组成

___.isalnum()判断指定字符串是否全部由字母和数字组成

'''
print('1',s.isidentifier())  #s = 'hello,world' 有个逗号
s5 = 'helloworld'
print('2',s5.isidentifier())


