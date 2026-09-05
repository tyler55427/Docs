# gcd

## 题目名称

**问题描述**：求两个正整数 a 和 b 的最大公约数（GCD）。

**解法**：使用欧几里得算法（辗转相除法）。基于定理：gcd(a, b) = gcd(b, a % b)，当 a % b == 0 时，b 即为最大公约数。

```cpp
int gcd(int a,int b)
{
	return a%b==0?b:gcd(b,a%b);
}

int main() {  // 必须是 int main()
    int a, b;
    cout << "请输入两个整数: ";
    cin >> a >> b;
    cout << "gcd = " << gcd(a, b) << endl;
    return 0;
}
```

**备注**：

- 时间复杂度：O(log min(a, b))
- 可扩展为扩展欧几里得算法求逆元
