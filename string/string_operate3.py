'''字符串的切片操作'''#会产生新的对象
#字符串是不可变序列，无 增 删 改
s='hello,Python'
s1=s[:5]
print(s1) #切到第五位置

s2=s[6:] #从6位开始切
print(s2)

print(id(s))
print(id(s1))
print(id(s2))

print('___________切片[start:end:step]__________')
print(s[::-1]) #从-1倒过来写

'''_________格式化字符串___________'''
#why ：文档中有些不用变的东西
'''
%s      为字符串的占位符   如  我的名字叫：%s,今年 %d岁 &（name age）为实际值
%i或%d  为整数的占位符
%f      为浮点数的占位符
'''

#如下 %作占位符

name='张三'
age=18
print('我叫%s，今年%d岁' % (name,age))  #中间的%为固定符号
#{}作占位符
print('我叫{},今年{}'.format(name,age)) #format前面是个点

#f-string (python3)
print(f'my name is {name}, I am {age} years old')

#宽度
print('%10d' % 99) #宽度为10

#小数的精度
print('%f' % 3.1415926)
print('%.3f' % 3.1415926) #保留三位小数

s='你真的很帅' #注意编码与解码的格式要相同
#编码
print(s.encode(encoding='GBK')) #GBK一个中文两个字节
print(s.encode(encoding='UTF-8'))  #UTF-8中 一个中文占三个字节

#解码
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))

name=input('请输入你的名字')
age=int(input('请输入你的年龄'))
print('我叫%s，今年%d岁' % (name,age))  #中间的%为固定符号
#{}作占位符
print('我叫{},今年{}'.format(name,age)) #format前面是个点
