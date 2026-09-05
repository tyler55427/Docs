# 数位DP

**问题描述**：给定区间 [l, r]，统计 0-9 每个数字在所有整数中出现的次数。

**解法**：数位 DP（按位统计），将数字拆分为各位，按每一位的贡献累加，利用预计算避免重复计算。

```cpp
constexpr int MAX_DIGITS = 15;  // 最多 15 位（long long 范围）
using ll = long long;

ll l, r;

// mi[i] = 10^i（10 的 i 次幂）
// dp[i] = 在所有 i 位数（000..0 到 999..9）中，每个数字出现的总次数
//        = 10^(i-1) * 10 + dp[i-1] * 10
//        = 每个数字在最高位出现 10^(i-1) 次 + 在剩余位出现 dp[i-1] 次 * 10 个数
ll mi[MAX_DIGITS];
ll dp[MAX_DIGITS];

// ans[10] 统计每个数字出现的次数
ll ansHigh[MAX_DIGITS], ansLow[MAX_DIGITS];
int digits[MAX_DIGITS];  // 存储数字 n 的每一位（digits[1] 为最低位）

// 统计 [0, n] 范围内每个数字出现的次数
// 思路：按位分解数字，从高位到低位累加每个位置的贡献
void countDigits(ll n, ll* ans)
{
    if (n < 0) return;  // 边界：l-1 可能为负

    ll tmp = n;         // 剩余未处理的部分
    int len = 0;        // 数字位数

    // 提取每一位：digits[1] = 最低位，digits[len] = 最高位
    while (n)
    {
        digits[++len] = n % 10;
        n /= 10;
    }

    // 从高位到低位处理
    for (int i = len; i >= 1; --i)
    {
        int cur = digits[i];  // 当前位的数字

        // 第1步：当前位之前的"高位"部分，对每个数字的贡献
        // 范围 [0, 999] 共 1000 个数，每位上每个数字出现 mi[i-1]=100 次
        // 共有 cur 个完整的"高位循环"，每个循环贡献 mi[i-1] 次
        for (int d = 0; d < 10; ++d)
            ans[d] += dp[i - 1] * cur;

        // 第2步：当前位本身的贡献（比当前位小的数字）
        // 当高位相同、当前位 < cur 时，完全循环了 mi[i-1] 次
        for (int d = 0; d < cur; ++d)
            ans[d] += mi[i - 1];

        // 第3步：当前位等于 cur 时，累加"低位的实际数值"部分
        // tmp 是去掉高位后的剩余值（低位部分的实际值）
        tmp -= mi[i - 1] * cur;
        ans[cur] += tmp + 1;  // +1 是因为还要算上 0 这个值

        // 第4步：处理前导0
        // 当 j=0 时，第2步多加了 mi[i-1]，但前导0不应该计入
        // 因为在 i 位数的表示中，最高位不能为 0（如 007 是 7，不是3位数）
        // 所以要减去这些"被错误计入"的前导0
        ans[0] -= mi[i - 1];
    }
}

int main()
{
    scanf("%lld%lld", &l, &r);

    // 预计算：mi[i] = 10^i，dp[i] = 每个数字在 i 位数中出现的总次数
    mi[0] = 1;
    for (int i = 1; i <= 13; ++i)
    {
        dp[i] = dp[i - 1] * 10 + mi[i - 1];
        mi[i] = 10 * mi[i - 1];
    }

    // 用数位 DP 分别统计 [0, r] 和 [0, l-1]，相减得到 [l, r]
    countDigits(r, ansHigh);
    countDigits(l - 1, ansLow);

    // 输出 0-9 每个数字在 [l, r] 范围内出现的次数
    for (int d = 0; d < 10; ++d)
        printf("%lld ", ansHigh[d] - ansLow[d]);
    return 0;
}
```
