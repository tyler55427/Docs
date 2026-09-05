# 输出的几种方式
a=10
print('I am',a,'years old')
print('I am '+str(a)+' years old')
print('I am %d years old' % a) # 常用
print('I am {} years old'.format(a))
print(f'I am {a} years old') # 常用



# 作用域调试
## 第一个按钮，到下一个断点
## 第二个按钮，执行完这一行，不会进入函数内部
## 第三个按钮，可以进入函数内部，逐语句运行
## 第四个按钮，可以在函数内部将函数运行完，退出函数

"""dfaskdjf;lsakdjf;alksdf"""
x = 1
def fun1():
    """aaaaaaaaaaa"""
    # 报错，因为x没有声明为全局变量
    print(x)
    x=2

def fun2():
    global x
    print(x)
    x=2

fun2()
print(x)

# lambda表达式
## 第一个参数使传入的参数，第二个参数使返回值（不用return）
f = lambda x:x+1
print(f(20))

f1 = lambda x,y:x*y
print(f1(2,3))

# 异常

try:
    print(3/0)
except:
  print("出错啦！")  




# 课堂内容（书上还真没有）

# 函数调用的两种参数传递方式，位置参数 和 关键字参数
def test(a,b):
    print(a,b)

test(1,2)
test(b=2,a=1)
# 位置参数必须在关键字参数之前
# test(a=1,2) 会报错

# 函数参数的两种符号，/ 和 *
# / 之前的参数只能通过位置参数传递
# * 之后的参数只能通过关键字参数传递
def test(a,b,/,c,d,e,*,f):
    print(a,b,c,d,e,f)

test(1,2,3,4,5,f=6)
test(1,2,c=3,d=4,e=5,f=6)
# test(1,2,c=3,d=4,e=5,6) 会报错
# test(a=1,2,3,4,5,f=6) 会报错
print()


def test(a,b,c=3):
    """This is a test function
    a,b,c are all int
    """
    print(a,b,c)

print(test.__doc__) # 输出函数的帮助文档
help(test) # 输出函数的帮助文档

b=10
def test():
    b=5 # 局部变量，不会改变全局变量，这是和C++的区别
    print(b)
    # global b   # 有了局部变量，就不能再声明全局变量
    # print(b)
    # b=20
    # print(b)

test()
print(b)
print()

# 一个*表示元组
# 就算是传入列表，也会被打包成元组
def test(*x):
    print(x)
    print(type(x))
# 两个*表示字典
def test(**x):
    print(x)
    print(type(x))


# 列表
# 命名规则：列表名用复数，元素名用单数
x=['a','b','c','d','e']


# 增
x.append('f')  # 在末尾添加
x.insert(0,'z') # 在第0个位置插入
x.extend(['g','h']) # 用列表扩展列表
x+=['i','j'] # 用列表扩展列表

# 删
x=['a','b','c','d','e','f','g','h']
x.pop() # 删除最后一个元素
x.pop(1) # 删除第1个元素
x.remove('a') # 删除第一个出现的元素
del x[0] # 删除第0个元素 
# del x# 删除整个列表，x不存在，不能print
x.clear() # 清空列表，x存在，可以print

# 改
x=['a','b','c','d','e','f','g','h']
# 复制
y=x # y和x指向同一个列表
print(id(x),id(y))
print(hex(id(x)),hex(id(y)))
print(x is y)

y=x.copy() # y和x指向不同的列表
y=x[:] # y和x指向不同的列表
print(id(x),id(y))
print(hex(id(x)),hex(id(y)))
print(x is y)

# 查
print(x.index('d')) # 查找元素的位置
print(x.count('d')) # 查找元素的个数
print('a' in x) # 判断元素是否在列表中
print('a' not in x) # 判断元素是否不在列表中
print(x[0]) # 输出第0个元素
print(x[-1]) # 输出最后一个元素
# 切片
print(x[1:3]) # 输出第1个到第3个元素，切片可以越界，不会报错
print(x[1:]) # 输出第1个到最后一个元素
print(x[:3]) # 输出第0个到第3个元素
print(x[:]) # 输出全部
print(x[::2]) # 输出全部，步长为2
print(x[::-1]) # 逆序输出
print(x[1:3:2]) # 输出第1个到第3个元素，步长为2


# 排序
x=['a','b','c','f','g','d','e','h']
x.sort() # 排序，改变原列表，不返回值
x.sort(reverse=True) # 逆序排序
x=sorted(x) # 排序，不改变原列表，返回一个新列表
x=sorted(x,reverse=True) # 逆序排序，不改变原列表

x.reverse() # 逆序
print(x)
len(x) # 列表长度
list(range(10)) # 生成一个0-9的列表，range是一个迭代器，不是列表，但是可以用列表的方法

# range
# 5个方法
x=range(10)
x.count(1) # 1出现的次数
x.index(1) # 1的位置
x.start # 开始，默认为0
x.stop # 结束，不包括这个数
x.step # 步长，默认为1

print(sum(range(101))) # 求和

# 元组，tuple
# 元组是 不可变 的列表
x=('a','b','c','d','e','f','g','h')
# x='a','b','c','d','e','f','g','h' # 也可以这样定义，但是不推荐
x=(1) # 这样定义的是一个int，不是元组
print(type(x))
x=(1,) # 这样定义的是一个元组
print(type(x))
# 元组的方法和列表的方法一样，但是不能增删改，只能查
x=('a','b','c','d','e','f','g','h')
x.count('a')
x.index('a')

def fun(*x):# *x表示可以传入任意多个参数，传入的参数会被打包成一个元组
    print(x)




# 使用dir()函数查看对象的属性和方法
# 有两个_的方法和属性是私有的，不建议使用
# 有一个_的方法和属性是保护的，不建议使用 
# 没有_的方法和属性是公有的，可以使用
# 使用help(lsit.__le__)查看方法的帮助文档，可以看到方法的参数和返回值
# 直接用dir()可以查看当前脚本的所有对象，包括变量、函数、类等，可以删除不要的对象

# 序列化对象共享一些类似的相同的方法，如可以使用索引访问
# 对象分为可变对象和不可变对象，range(),str(),tuple()是不可变对象，list(),dict(),set()是可变对象
# 内置函数可以操作很多对象

# 列表推导式
x=[[1,2,3],[4,5,6],[7,8,9]]
# 第二列
y=[i[1] for i in x]
# 对角线
y=[x[i][i] for i in range(3)]
# 加上判断条件，取偶数
y=[x[i][i] for i in range(3) if x[i][i]%2==0]
# 判断条件可以放在前面
y=[x[i][i] if x[i][i]%2==0 else 0 for i in range(3)]
# 两层循环
y=[x[i][j] for i in range(3) for j in range(3) if x[i][j]%2==0 and i==j] 
y=[sum(x[i]) for i in range(3)] # 求和
# 对每一列求和
y=[sum([i[y] for i in x]) for y in range(3)]

# 字典
x={'a':1,'b':2,'c':3}
# 重复的键会被覆盖
x={'a':3,'a':2,'c':1,'b':3}
sorted(x) # 对键排序
print(sorted(x.keys())) # 对键排序，和上面等价，最后出来的结果也只有键，返回的是列表
print(sorted(x.values())) # 对值排序
print(sorted(x.items())) # 对键值对排序，返回一个元组
print(x)
print(sorted(x.items(),key=lambda x:x[1],reverse=True)) # 对值排序

# 数值（浮点数的精度问题）
x=23.24+345.45
print(x)
# 使用自带函数解决
round(x,1) # 取小数点后1位
round(x,2) # 取小数点后2位
round(x,-1) # 取整十，向前取整
print(round(x))

# python 支持很大的数值(4300位数)
print(2**10000)

# 4种舍入方式
# round()默认的舍入方式是round_half_even
# 总体上是四舍五入，向偶数（向二进制的最后一位是0的方向）舍入
print(round(1.5)) # 1.1 有两个方向 01.0 和 10.0，选择后面那个
print(round(2.5))
print(round(3.5)) 
# round_half_up 向上舍入，math.ceil()
# round_half_down 向下舍入，//整除运算，math.floor()
# round_away_from_zero
# round_half_even
# 向0舍入，C语言的整数之间的运算，正负数都向0舍入

# Decimal 固定精度
import decimal
decimal.Decimal('0.1')
# Fraction 分数
import fractions
fractions.Fraction(1,3)

# 集合
# 不是序列对象，不可变对象
# 特点
# 1. 无序
# 2. 不可变的
# 3. 元素可以是任意类型
# 4. 元素不能重复
# 5. 集合运算
langs={'c','c','a','sdf'}
print(langs)
# 可以将列表转化为集合
x=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
y=set(x)
print(y)
# 集合运算
x={1,2,3,4,5}
y={4,5,6,7,8}
print(x|y) # 并集
print(x&y) # 交集
print(x-y) # 差集
print(x^y) # 对称差集
print(x>y) # 判断是否是子集
print(x<y) # 判断是否是超集
print(x>=y) # 判断是否是子集
print(x<=y) # 判断是否是超集
print(x==y) # 判断是否相等
print(x!=y) # 判断是否不相等
print(x.isdisjoint(y)) # 判断是否没有交集
x.add(6) # 添加元素
x.remove(6) # 删除元素
x.discard(6) # 删除元素，如果不存在不会报错
x.pop() # 删除一个元素，随机删除
x.clear() # 清空集合
x.update({6,7,8}) # 添加多个元素

D={'a':1,'b':2,'c':3}
D['a']
D.get('d')
'd' in D
'a' in D
value=D['d'] if 'd' in D else 0 # 三目运算符
