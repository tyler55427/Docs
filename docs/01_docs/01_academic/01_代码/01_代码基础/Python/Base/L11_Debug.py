# 调试

# 两种：查看日志 和 断言

import traceback

# 抛出异常
try:
    raise Exception('This is an error message.')
except Exception as err: # 和import相同的别名方式
    # 在处理异常的同时，得到回溯序列。例如用于写入日志
    print(traceback.format_exc())
    print('Error happened: ' + str(err))


# 回溯：遇到错误，生成一些错误信息
# 调用栈序列：包含错误信息、代码行号、函数调用的序列





# 断言
# assert：条件 ， 条件为False的显示的字符串
# 可以加上-O选项运行，忽略assert
assert 1==1.0,'jiushibudengyu'





# 日志
# logging模块
## 日志级别：debug、info、warning、error、critical
## 禁用日志disable