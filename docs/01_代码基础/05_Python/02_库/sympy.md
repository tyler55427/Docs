# 符号推导 sympy

能够进行符号运算、矩阵运算、因式分解和展开、可以数值和符号相乘

```python
from sympy import symbols, Matrix, expand, factor, solve
c1 = symbols('c1')  # 符号变量
s1 = symbols('s1')  # 符号变量
c2 = symbols('c2')  # 符号变量
s2 = symbols('s2')  # 符号变量
c3 = symbols('c3')  # 符号变量
s3 = symbols('s3')  # 符号变量
c23 = symbols('c23')  # 符号变量
s23 = symbols('s23')  # 符号变量
l1 = symbols('l1')  # 符号变量
l2 = symbols('l2')  # 符号变量
l3 = symbols('l3')
T = Matrix([[c1*c23,-c1*s23,s1,c1*(c2*l2+l1)],[s1*c23,-s1*s23,-c1,s1*(c2*l2+l1)],
            [s23,c23,0,s2*l2],[0,0,0,1]])  # 符号矩阵
px = symbols('l3')  # 符号变量
py = 0 # 符号变量
pz = 0  # 符号变量
P = Matrix([[px],[py],[pz],[1]])  # 符号矩阵
res = T * P  # 符号矩阵乘法

# 因式分解所有元素
res = res.applyfunc(factor)
print("因式分解后:\n", res)
for i in res:
    print(i)

# 展开所有元素
res = res.applyfunc(expand)
print("展开后:\n", res)
for i in res:
    print(i)

# 叉乘
v1 = Matrix([c1*c23, s1*c23, s23])  # 符号矩阵
v2 = Matrix([-c1*s23, -s1*s23, c23])  # 符号矩阵
v3 = v1.cross(v2)  # 符号矩阵叉乘

eq1 = l2*s2 + l3*s2*c3 + l3*c2*s3 - pz
eq2 = l1 + l2*c2 + l3*c2*c3 - l3*s2*s3 - px/c1
solution = solve((eq1, eq2), (c3, s3))
print(solution[c3])
print(solution[s3])
```

```
因式分解后:
 Matrix([[c1*(c2*l2 + c23*l3 + l1)], [s1*(c2*l2 + c23*l3 + l1)], [l2*s2 + l3*s23], [1]])
c1*(c2*l2 + c23*l3 + l1)
s1*(c2*l2 + c23*l3 + l1)
l2*s2 + l3*s23
1
展开后:
 Matrix([[c1*c2*l2 + c1*c23*l3 + c1*l1], [c2*l2*s1 + c23*l3*s1 + l1*s1], [l2*s2 + l3*s23], [1]])
c1*c2*l2 + c1*c23*l3 + c1*l1
c2*l2*s1 + c23*l3*s1 + l1*s1
l2*s2 + l3*s23
1
(-c1*c2**2*l2 - c1*c2*l1 - c1*l2*s2**2 + c2*l3)/(c1*c2**2*l3 + c1*l3*s2**2)
(c1*l1*s2 - l3*s2)/(c1*c2**2*l3 + c1*l3*s2**2)
```
