def test(a):
    # 不会换行，默认以换行为结尾
    print(a,end=' ')
    # 如果传入多个参数，自动在每个参数之间加上空格
    print(a,a,a)
    # 替换默认的空格
    print(a,a,sep=',',end='')
    print(';')
    # 声明该变量为全局变量（已经创建）
    global tttt
    # 函数都有返回值，如果没有写，则编译器默认加上return None
    return a
test('hello')
print()

a=10
def aa():
    #   python中会报错，但C++不会
    print(a)
    a=5

# 可以返回不同的值
def aa(temp):
    if temp==1:
        return 'temp=1'
    else:
        return 1

print(aa(9))
print()

# 异常
def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument!')
# 异常keyboardInterrupt，用户使用Ctrl+C打断
print()










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