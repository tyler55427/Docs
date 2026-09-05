# 正则表达式（regex）
# 正则表达式的使用要导入re模块

import re

phone = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# 找到返回一个Match对象，没找到返回None
mo = phone.search('My number is 415-555-4242.')
# Match对象有一个gruop方法，group()方法返回实际匹配的文本
print('Phone number found: ' + mo.group())

# 用括号分组
# 匹配括号字符，需要转义
phone = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
# group(0)或group()返回整个匹配的文本
print(mo.group(0))
# groups()返回一个包含所有分组的元组
print(mo.groups())


# 特殊含义字符

# . 匹配除换行符之外的所有字符
# ^ 匹配字符串开始
# $ 匹配字符串结束
# ? 匹配0次或1次
# * 匹配0次或多次
# + 匹配1次或多次
# {} 匹配特定次数
# [] 匹配指定字符集
# | 匹配多个正则表达式中的一个
# () 分组



# 1. 用管道匹配多个分组
# 字符|称为管道，匹配管道前后的任意一个分组
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())


# 2. 用问号实现可选匹配
# 问号表示匹配0次或1次，即该分组是可选的
# 问号 前 的分组是可选的
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

# 3. 用星号匹配零次或多次
# 星号表示匹配0次或多次
# 星号 前 的分组出现0次或多次
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

# 4. 用加号匹配一次或多次
# 加号表示匹配1次或多次
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1 == None)
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

# 5. 用花括号匹配 特定 次数
# 花括号表示匹配 特定 次数

# {n} 匹配n次

# 也可以匹配一个范围
# {n, m} 匹配n到m次
# {n, } 匹配n次以上
# {, m} 匹配m次以下


# 6. 贪心和非贪心匹配
# 正则表达式默认是贪心的，即匹配尽可能多的文本
# 在花括号后加上 问号，使其变为非贪心的
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
# 5个Ha
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
# 3个Ha
print(mo2.group())

# 7. findall()方法
# search()方法返回一个Match对象，只返回第一个匹配的文本
# findall()方法返回一个字符串列表，包含所有匹配的文本，没有 分组 时返回一个字符串列表
# 有 分组 时返回一个元组列表


phone = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

phone = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phone.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

# 8. 字符分类

# digit字符，0-9的任何数字
# \d 0-9的任何数字
# \D 除0-9的任何字符

# word字符，字母、数字、下划线
# \w 任何字母、数字或下划线字符（可以认为是匹配单词字符）
# \W 除字母、数字、下划线的任何字符

# space字符，空格、制表符、换行符
# \s 空格、制表符或换行符（可以认为是匹配空白字符）
# \S 除空格、制表符、换行符的任何字符

# 匹配固定数字，[0-5]匹配0到5的数字
# 只匹配字母，[a-zA-Z]匹配所有大小写字母

# 9. 创建自己的字符分类
# 用方括号创建自己的字符分类
# [aeiou]匹配所有元音字母，是 一个 元音字母就匹配
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

# 普通的正则表达式字符在方括号中没有特殊含义，不需要转义
# [0-5.]匹配0到5的数字或者句号

# 非字符类
# 在字符类的方括号开头加上^，表示非字符类
vowelRegex = re.compile(r'[^aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)


# 10. 插入字符和美元字符
# ^匹配字符串的开始，匹配的文本必须出现在字符串的开始
# $匹配字符串的结束，匹配的文本必须出现在字符串的结束
beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello world!')
print(mo.group())
mo = beginsWithHello.search('He said hello.')
print(mo == None)

endsWithNumber = re.compile(r'\d$')
mo = endsWithNumber.search('Your number is 42')
print(mo.group())
mo = endsWithNumber.search('Your number is forty two.')
print(mo == None)

# ^和$一起使用，匹配整个字符串


# 11. 通配字符
# .匹配除 换行符 之外的所有字符，只匹配一个字符
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

# 12. 用点-星匹配所有字符
# .*匹配所有字符，除换行符；任意文本
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

# 加上问号，使其变为非贪心
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

# 13. 用句点字符匹配换行
# .匹配除换行符之外的所有字符，匹配到换行符就停止
# re.DOTALL作为re.compile()的第二个参数，匹配所有字符
noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo.group())
newlineRegex = re.compile('.*', re.DOTALL)
mo = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo.group())


# 14. 不区分大小写的匹配
# re.IGNORECASE 或 re.I 作为re.compile()的第二个参数，不区分大小写
robocop = re.compile(r'robocop', re.I)
mo = robocop.search('RoboCop is part man, part machine, all cop.')
print(mo.group())
mo = robocop.search('ROBOCOP protects the innocent.')
print(mo.group())
mo = robocop.search('Al, why does your programming book talk about robocop so much?')
print(mo.group())

# 15. 用sub()方法替换字符串
# sub()方法返回替换后的字符串
# 第一个参数是要替换的字符串，第二个参数是替换成的字符串
# sub()方法返回一个新的字符串，原字符串不变
# compilel函数里面的r是用来表示原始字符串的，不用转义
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo)


# 16. 管理复杂的正则表达式
# re.VERBOSE作为re.compile()的第二个参数，可以添加空白符和注释
# 用#号添加注释
# 多余的空白符会被忽略
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    \d{3} # first 3 digits
    (\s|-|\.) # separator
    \d{4} # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)
mo = phoneRegex.search('My number is 415-555-4242.')
print(mo.group())

# 17. 组合使用re.IGNORECASE、re.DOTALL和re.VERBOSE
# re.IGNORECASE、re.DOTALL和re.VERBOSE可以组合使用
# 作为re.compile()的第二个参数，使用|连接，因为只能有一个第二个参数
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
mo = someRegexValue.search('Foo')
print(mo.group())
mo = someRegexValue.search('FOO')
print(mo.group())