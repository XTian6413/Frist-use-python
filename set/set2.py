#集合2
#判断 in/not in
s={10,20,30,40,50}
print(10 in s)
print(10 not in s )

#集合为可变序列————> 增 删 改

'''_______________增加_____________'''
s.add(60) #只可以增加一个
print(s)

s.update({100,200}) #update至少增加一个元素
s.update([500])    #放列表
#s.update((1000))   #放元组
print(s)

'''_____________删除___________'''
'''·调用remove()方法，一次删除一个指定元素（但一定要存在），如果指定的元素不存在抛出
KeyError
·调用discard()方法，一次删除一个指定元素，如果指定的元素不存在不会显示异常
·调用pop()方法，一次只删除一个任意元素(不能指定参数)
·调用clear()方法，清空集合'''

#s.remove(10)
#s.discard(100)
#s.pop() 随机删除 不能指定
#clear()