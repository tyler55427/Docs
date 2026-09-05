# 软件Bug期望

**问题描述**：一个软件有 s 个子系统，会产生 n 种 bug。某人一天发现一个 bug，这个 bug 属于某种 bug 分类，也属于某个子系统。每个 bug 属于某个子系统的概率是 $\frac{1}{s}$，属于某种 bug 分类的概率是 $\frac{1}{n}$。求发现 n 种 bug，且 s 个子系统都找到 bug 的期望天数。

**解法**：利用期望的线性性质，将相同 dp 移项后反推。

$$dp[i][j] = \frac{dp[i][j+1] \times i \times (s-j) + dp[i+1][j] \times (n-i) \times j + dp[i+1][j+1] \times (n-i) \times (s-j) + n \times s}{n \times s - i \times j}$$

```cpp
// 注意概率是浮点数
double dp[105][105]; // dp[i][j] 表示已经发现 i 种 bug 且 s 个子系统后，达到目标的期望天数

int solve(int s, int n)
{
    // 已经找到 n 种 bug 且 s 个子系统的期望天数为 0
    dp[n][s] = 0;
    for (int i = n; i >= 0; --i)
    {
        for (int j = s; j >= 0; --j)
        {
            // 防止越界
            if (i == n && j == s) continue;
            // // 找到相同的 bug 分类和子系统
            // dp[i][j] += (double)i / n * j / s * dp[i][j];
            // // 找到相同的 bug 分类但不同的子系统
            // dp[i][j] += (double)i / n * (s - j) / s * dp[i][j + 1];
            // // 找到不同的 bug 分类但相同的子系统
            // dp[i][j] += (double)(n - i) / n * j / s * dp[i + 1][j];
            // // 找到不同的 bug 分类和子系统
            // dp[i][j] += (double)(n - i) / n * (s - j) / s * dp[i + 1][j + 1];
            // // 计算期望天数
            // dp[i][j] += 1;

            // 根据期望的线性性质，将相同的dp[i][j]移项
            dp[i][j] = (dp[i][j + 1] * i * (s - j) +
                dp[i + 1][j] * (n - i) * j +
                dp[i + 1][j + 1] * (n - i) * (s - j) + n * s) /
                (n * s - i * j);
        }
    }
    return dp[0][0];
}
```
