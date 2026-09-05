# x=[[i+k for i in range(2)] for k in range(10)]
# print(x)
# print(dict(x))

# print({i:i**i for i in range(10)})

# x='aaabbbbdd'
# print(set(x))

# def f(a:int,b:int,c:str)->str:
#     return a+b

# print(f(2,3,'sd')==5)

# x=2.605
# for i in range(10):
#     x+=0.01
#     print(x,round(x,2))

# print('x'.upper(),'x'.lower(),'x'.title())

# from pathlib import Path
# p=Path('./temp.txt')
# p.unlink()


# from pathlib import Path   
# import json
# class MyError(Exception):
#     def __init__(self):
#         super().__init__()
#     def out(self):
#         return "错误：超出[0,100]有效范围"

# class MyError1(Exception):
#     def __init__(self):
#         super().__init__()
#     def out(self):
#         return "错误：输入错误超过两次"

# cnt=0
# l=[]
# try:
#     while len(l)<5:
#         x=int(input())
#         if x<0 or x>100:
#             cnt+=1
#             if cnt>2:
#                 raise MyError1
#         else:
#             l.append(x)
# except ValueError as e:
#     print('错误：输入非数字')
# except MyError1 as e:
#     print(e.out())
# except Exception as e:
#     print('错误：其他错误')
# finally:
#     p=Path('./scores.json')
#     p.touch()
#     p.write_text(json.dumps(l))

# print('''\
#     askjfd
#     falskdsadflkas
#     sdjfsal
# ''')

# x=90
# match x:
#     case 1:
#         print('1')
#     case 2:
#         print('2')

# i=1
# def f(x=i):
#     print(x)

# i=3
# f()
# def f(x,l=[]):
#     l.append(x)
#     return l
# print(f(1))
# print(f(2))
# print(f(3))

# matrix=[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# mt=[list(i) for i in zip(*matrix)]
# print(mt)

# while x:=input():
#     print(x)