# Catalan

## 题目名称

**问题描述**：求第 n 个 Catalan 数。Catalan 数序列：1, 1, 2, 5, 14, 42, ...（C(0)=1, C(1)=1, C(2)=2, ...）

**解法**：使用递归公式 C(n) = sum(C(i) * C(n-i-1))，其中 i 从 0 到 n-1。边界条件：C(0) = C(1) = 1。

```cpp
int c(int n)
{
	if(n==1||n==0) return 1;
	int res=0;
	for(int i=0;i<n;++i)
	{
		res+=c(i)*c(n-i-1);
	}
	return res;
}

int main()
{
	int n;
	cin>>n;
	cout<<c(n);
 }
```

**备注**：

- 该实现为递归版本，时间复杂度较高（指数级），适合小规模数据
- Catalan 数的递推公式也可写成 C(n) = C(n-1) * (4n-2) / (n+1)
- 常见应用：括号匹配、二叉树计数、卡特兰数与 Dyck 路径
