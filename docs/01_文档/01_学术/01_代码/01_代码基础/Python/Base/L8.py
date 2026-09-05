# 输入验证
# PyInputPlus 模块，需要额外安装
# pip install pyinputplus
# 1. 提示用户输入，直到用户输入有效为止
# 2. 可以提示次数限制，时间限制

# 几种输入验证函数
# inputStr() 输入字符串，自定义验证函数
# inputNum() 输入数字，返回int或float，取决于用户输入
# inputChoice() 输入选择，确保用户输入的是列表中的一个值
# inputMenu() 输入菜单，类似inputChoice()，但是会显示一个菜单，带有数字或字母标记
# inputYesNo() 输入yes或no，返回True或False
# inputBool() 输入True或False，返回True或False
# inputEmail() 输入电子邮件地址，返回字符串
# inputFilepath() 输入文件路径，返回字符串
# inputPassword() 输入密码，返回字符串，不会显示用户输入的内容

#import pyinputplus as pyip ，使用as关键字，可以给模块起别名
import pyinputplus as pyip


# 关键字参数min、max、greaterThan、lessThan
response = pyip.inputNum('Enter num: ', min=4) # 最小值为4，可以=4
response = pyip.inputNum('Enter num: ', greaterThan=4) # 大于4，不能=4

# 关键字参数blank
# 如果为True，允许用户不输入任何内容，直接按回车键
response = pyip.inputNum('Enter num: ', blank=True)

# 关键字参数limit、timeout、default
# limit：允许用户输入的次数
# timeout：允许用户输入的时间
# default：如果用户输入超时，使用默认值
response = pyip.inputNum('Enter num: ', limit=2, timeout=10, default=10)

# 关键字参数allowRegexes、blockRegexes
# allowRegexes：只允许匹配的正则表达式
# blockRegexes：不允许匹配的正则表达式
# 如果两个参数都提供，allowRegexes优先
response = pyip.inputNum('Enter num: ', allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
response = pyip.inputNum('Enter num: ', blockRegexes=[r'[02468]$'])

# 自定义验证函数，传给inputCustom()函数
# 将函数传给inputCustom()函数，而不是调用它

