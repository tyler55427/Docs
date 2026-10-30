# 使用矩阵求解线性方程组

```python
import numpy as np

A = np.array([[1, -2],[1, 3]])
Y = np.array([-1, 0])

# 求解线性方程组 AX = Y
if np.linalg.det(A) == 0:
    print("矩阵 A 是奇异的，无法求解线性方程组。")
X = np.linalg.solve(A, Y)

print(X)
```
