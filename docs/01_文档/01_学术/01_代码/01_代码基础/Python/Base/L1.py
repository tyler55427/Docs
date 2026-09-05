# 指数
print(2 ** 3)
# 整除
print(25 // 4)
print('hello world' + ' python')
print()

# 字符串复制
print('Python' * 5)
print()

a = 10
print(a)
a = '100'
print(a)
print()

# myname = input()
myname = '10'
print(len(myname))
# input()返回的总是字符串
print(int(myname) * 5)
print()

# 强制转换的函数
print('I am ' + str(29) + ' years old')
print(int('23'))
print(float('3.4'))
# 特殊
# 向0靠拢？ 且只有数字可以取整，字符串不行
print(int(-1.5))
print(int(1.5))
# 报错
# t = '3.3'
# print(int(t))
# print(int('9.9'))

print()

# 文本和数字相等判断
print(42 == '42')
print(42 == 42.0)
print(42 == 00042.000)
print()



# 输出的几种方式
a=10
print('I am',a,'years old')
print('I am '+str(a)+' years old')
print('I am %d years old' % a) # 常用
print('I am {} years old'.format(a))
print(f'I am {a} years old') # 常用
