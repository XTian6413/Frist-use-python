'''_________________-字符串的查询操作-__________________'''
s = 'hello,hello'  # 左边从零开始/右边从-1开始

print(s.index('lo'))  # 查询第一次出现的位置，找不到时会ValueError
print(s.find('lo'))  # 查询第一次出现的位置，找不到时会ValueError

# 以下两个均为查找最后一次的
print(s.rindex('lo'))
print(s.rfind('lo'))

# 推荐使用find和rfind #错误时返回-1 不会报错

'''————————————————字符串的替换与合并——————————————'''
s1 = 'hello Python'
print(s1.replace('Python', 'Java'))
s2 = 'hello Python,Python,Python'
print(s2.replace('Python', 'Jave', 2))  # 替换 两次 第三个差数为替换次数

# join()将列表或元组中的字符串 合并 成一个字符串
lst = ['hello', 'Java', 'Ptyhon']  # 列表
print('|'.join(lst))
print(''.join(lst))

t = ('hello', 'Java', 'Python')  # 元组
print('|'.join(t))
