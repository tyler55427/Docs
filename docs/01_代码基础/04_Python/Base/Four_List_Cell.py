# 4 列表
import copy
import random

# 加s表示这是一个列表
spam = ['cat','dog','elephant','rat']
print(spam[0])
print(spam[-1]) #最后一个，倒数
print(spam[0:1])
print(spam[:1])
print(spam[:])
print(len(spam))

spam = [['cat','dog'],[0,1]]
print(spam[1][0])

s1 = [1,2,3]
s2 = ['a','b','c']
s3 = s1 + s2
print(s3)
del s3[0]
print(s3)

for i in [2,4,76]:
    print(i)
print('a' in s2,'d' not in s2)

# 多重赋值，长度严格相等
a,b,c = s1
print(a,b,c,end=' ')
print()

# 返回索引和值
for index,item in enumerate(s1):
    print(index+1,item)

# 返回随机
print(random.choice(s2))
# 随机排序
random.shuffle(spam)
print(spam)

# 返回索引
print(s2.index('b'))
s2.append('d')
s2.insert(4,'e')
# 多次出现，只会删除第一次的
s2.remove('e')
s2.sort(reverse=True)
s2.reverse()
print(s2)

# 列表和字符串
str = 'apple'
print(str[2])
# str[2] = '4'   报错，不能更改






# 元组（输入使用圆括号）
# 元组是 不可变 的
eggs = ('qwe','asd')
print(eggs)
# 元组与不同元素的区别（一个元素的时候）
print(type(('hello')))
print(type(('hello',)))

list(('apple')) # 返回列表
tuple(['apple']) # 返回元组

# 引用
# 整数会复制，列表是同一个引用
spam = 41
cheese = spam
spam = 100
print(spam,cheese)

# 返回内存地址
print(id(42))
print()

# 函数传入列表会改变外部，引用的复制还是同一个列表
# 使用copy.copy()函数
the = copy.copy(spam)
print(the)
# 包含列表，使用深拷贝
the = copy.deepcopy(spam)
