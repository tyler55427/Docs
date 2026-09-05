# Python 导入问题与解决方案

## 一、导入机制

导入时按以下顺序搜索，**该顺序即 `sys.path` 列表的内容**：

1. 脚本所在目录，而非工作目录
2. 环境变量 `PYTHONPATH` 指定的路径
3. 标准库目录
4. 第三方库目录（site-packages）

## 二、`__init__.py` 的作用

`__init__.py` 区分**常规包**与**命名空间包**，并非"能否导入"的开关：

- **无 `__init__.py`** → 命名空间包（namespace package，Python 3.3+ PEP 420），**仍可正常导入**，可以通过`路径+函数`方式使用
- **有 `__init__.py`** → 常规包（regular package），具备下列作用：
  - 1. **包初始化**：`import` 包时自动执行其中的代码
  - 2. **控制导出**：通过 `__all__` 列表限制 `from 包 import *` 能导入哪些名称
  - 3. **汇总子模块 API**：在包入口统一导入子模块，`import 包` 后即可直接使用，无需再显式导入子模块

```python
# mypackage/__init__.py
from .a import func_a        # import mypackage 后直接 mypackage.func_a()
__all__ = ["func_a"]         # from mypackage import * 只导出 func_a
```

## 三、绝对导入 vs 相对导入

### 绝对导入

- `import utils`：按 `sys.path` 找，任何位置可用

### 相对导入

- `from . import utils`：相对当前包所在的目录，常用于功能包内部
- 直接运行带有相对导入的脚本会报错，可通过以下方式解决：
  - 添加路径到`sys.path`中，然后修改相对导入为绝对导入
  - `python -m mypackage.a` 会将`mypackage`识别为包，然后以此作为`.`的相对路径，所以不能直接`python -m a`

# 四、工作目录和脚本目录

- 工作目录：`.`目录和`os.getcwd())`
- 文件目录：`sys.path[0]`和 `os.path.dirname(os.path.abspath(__file__))`
