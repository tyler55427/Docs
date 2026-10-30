# 输入验证：PyInputPlus

> 第三方库，需先安装：`pip install pyinputplus`
>
> 提示用户输入，**直到输入有效为止**，可配合次数/时间限制。

```python
import pyinputplus as pyip       # 用 as 起别名
```

## 常用输入函数

| 函数 | 说明 |
| --- | --- |
| `inputStr()` | 字符串，可自定义验证函数 |
| `inputNum()` | 数字，按输入返回 `int` 或 `float` |
| `inputChoice()` | 必须是给定列表中的一个值 |
| `inputMenu()` | 类似 `inputChoice()`，但显示带数字/字母标记的菜单 |
| `inputYesNo()` | yes/no，返回 `True/False` |
| `inputBool()` | True/False |
| `inputEmail()` | 邮箱 |
| `inputFilepath()` | 文件路径 |
| `inputPassword()` | 密码，输入时不显示 |

## 关键字参数

```python
# 数值范围
pyip.inputNum('Enter num: ', min=4)              # 最小 4（包含）
pyip.inputNum('Enter num: ', greaterThan=4)      # 严格大于 4

# 允许空
pyip.inputNum('Enter num: ', blank=True)

# 限制次数 / 超时 / 默认值
pyip.inputNum('Enter num: ', limit=2, timeout=10, default=10)

# 正则白名单 / 黑名单（同时给定时白名单优先）
pyip.inputNum('Enter num: ', allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
pyip.inputNum('Enter num: ', blockRegexes=[r'[02468]$'])
```

## 自定义验证

把验证函数传给 `inputCustom()`，**传函数本身，不要带括号调用**：

```python
def valid(s):
    return s in ['yes', 'no']

pyip.inputCustom('Continue? ', valid)
```