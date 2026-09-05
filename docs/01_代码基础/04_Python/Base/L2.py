# boolean
# 首字母大写
Pan_Duan = True
print(Pan_Duan)
print()

# 布尔运算符
print(True and True)
print(False or False)
print(not False)
# 顺序，not>and>or
print()

# 代码块
# :结尾，以代码块的缩进作为是否为同一个内容的判断
temp = '1'
if temp == '3':
    print(1)
    print(2)
elif temp == '2':
    print(3)
else:
    print(4)
print()

# 循环
temp = 5
while temp > 0:
    temp -= 1
    if temp == 1:
        break
    print(temp)
    if temp ==3:
        continue
    print('hello')
# 被认为是False的，0、0.0、''（没有空格）
# 还有空列表，空元组，空字典

if ' ':
    print('dfgsdfg')
# 判断的高级用法
if 1 < 2 < 3:
    print('yes')

# 从0到5，左闭右开
for i in range(5):
    print(i)
# 头尾
for i in range(12,16):
    print(i)
# 头尾，步长
for i in range(10,100,20):
    print(i)
for i in range(3,-3,-1):
    print(i)
print()

# 导入模块
import random
# 可以使函数的调用不用加上random.前缀
# from random import *;
import sys
for i in range(5):
    # 两个整数之间的随机数
    temp = random.randint(1,10)
    print(temp)
    # if temp == 7:
    #     print('退出')
    #     sys.exit()
print()
