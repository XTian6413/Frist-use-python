#集合之间的关系
#两个集合是否相等 ————》元素相等
s={10,20,30}
s1={20,30,10}
print(s==s1)
print(s!=s1)
'''·两个集合是否相等
·可以使用运算符==或!=进行判断
一个集合是否是另一个集合的子集
·可以调用方法issubseti行判断
·B是A的子集
·一个集合是否是另一个集合的超集
·可以调用方法issuperset行判断
·A是B的超集
·两个集合是否没有交集
·可以调用方法isdisjointi行判断
'''
s3={10,20,30,40,50,60,70}
s4={20,30,40,50}
s5={50,60,70,80}
print(s4.issubset(s3)) #翻译过来就是 s4是s3的子集吗？Ture  /数学关系 s3是s4的超集
print(s3.isdisjoint(s4)) #s3和s4是否没有交集 ————否 ——s3和s4有交集
print('S3:',s3)
print('S4:',s4)
'''求交集'''
print('S3与S4的交集',s3.intersection(s4)) #intersection()和 & 等价， 交集操作
print(s4.intersection(s3))
print(s3 & s4)
print(s4 & s3)
'''求并集'''
print(s3.union(s5))  #union与|等价，并集操作
print(s3 | s5)
'''差集'''
print(s3.difference(s4))
print(s3-s4)
'''对称交集'''#去掉并集
print(s3.symmetric_difference(s4))
print(s3^s4)

'''______________集合生成式____________'''
set1={i for i in range(6)}
print(set1)
set2=[i*i for i in range(6)]
print(set2)
'''______________列表生成式____________''' #花括号变成方括号
lst1=[i for i in range(6)]
print(lst1)

lst2=[i*i for i in range(6)]
print(lst2)

