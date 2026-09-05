# 字符串操作

# 单双引号都可以表示字符串，当只有一个要转义的时候，可以这样用

print("This's a Tree.")
print('This\'s a Tree.')

# 前面加上r输出原始字符串，包括转义字符
print(r'T\'t')

# 多行字符串，单双引号都可以，保留所有空格和换行
# 单引号不用转义
print('''
      hello'' world
    1232
      
      ''')

'''
这里是多行注释
'''

# 字符串切片
spam = 'Hello World!'
fizz = spam[0:5]
print(fizz)

# in 和 not in
print('he' in fizz)

# 字符串插值
print('My name is %s. I\'m %d years old.' % ('Alice',20))
name = 'AI'
year = 24
# f是format的缩写，可以直接在字符串中插入变量，用{}括起来
print(f'My name is {name}. I am {year+10} years old')

# 有用方法
print(spam.upper())
print(spam.lower())

print('h'.islower())

# 只有字母
print('sdf'.isalpha())
# 只有字母 和 数字
print('df2'.isalnum())
# 只有数字
print('23243'.isdecimal())
# 只有空格 制表符 换行符
print('     \n'.isspace())
# 以大写字母开头，后面都是小写字母的单词 或 数字 或 空格
print('Tdskf 8776 Tkk'.istitle())
print('Tdskf 8776 fd'.istitle())
print('Tdskf 8776j '.istitle())

print()

# 检查部分
print('The street is broad.'.startswith('The'))
print('The street is broad.'.endswith('d.'))

# join split
spam = ['My','name','is','AI']
print(' '.join(spam))
spam = 'My namne is AI.'
print(spam.split('e')) # 默认空白字符

# 轴分隔
print(spam.partition('n')) # 只分隔第一次出现；如果没有，第一个是整个字符串

# 对其文本
print(spam.rjust(20,'d')) # 默认空格，第一个参数是总数
print(spam.ljust(20,'d'))
print(spam.center(21,'-'))
print()

# 删除空白字符
spam = '    Hello world     '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())
spam = 'spamspamHellospamspam'
print(spam.strip('msap')) # 顺序不重要
print()

# 字符数值
print(ord('A'))
print(chr(65))