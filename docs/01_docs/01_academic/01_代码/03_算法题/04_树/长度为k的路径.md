# 长度为k的路径

**问题描述**：给定一棵有 n 个节点的树，求树中长度为 k 的路径数量。

**解法**：树形 DP。`dp[u][len]` 表示以 u 为根的子树中，从 u 出发向下、路径长度恰好为 len 的路径条数。

## 全局变量

- `tree[MAXN]`：邻接表存储无向树
- `dp[u][len]`：以 u 为根的子树中，从 u 出发向下、路径长度恰好为 len 的路径条数
- `ans`：整棵树中长度为 k 的路径总数（所有方向）

```cpp
const int MAXN = 50005;
const int MAXK = 510;

vector<int> tree[MAXN];
int dp[MAXN][MAXK];
long long ans;
```

## DFS

`dp[u][0] = 1`：从 u 出发、长度为 0 的路径只有 1 条（就是 u 自己）。

遍历子节点 v，先递归处理子树，再累加经过 u 的路径条数，最后将 v 子树的路径合并到 u。

```cpp
void dfs(int u, int fa, int k)
{
    // 从 u 出发、长度为 0 的路径只有 1 条(就是 u 自己)
    dp[u][0] = 1;

    for (int i = 0; i < (int)tree[u].size(); ++i)
    {
        int v = tree[u][i];
        if (v == fa) continue;        // 不走回父结点

        dfs(v, u, k);

        // 先把 v 子树中"以 u 为拐点"的长度为 k 的路径累加到 ans
        // 只在根节点进行统计，防止重复
        // 这些路径由 v 子树中长度为 j 的向下路径,和 u 另一子树中长度为 (k-j-1) 的向下路径拼接而成
        for (int j = 0; j < k; ++j)
        {
            ans += (long long)dp[v][j] * dp[u][k - j - 1];
        }

        // 再把 v 子树中的路径合并到 u 上:u 出发向下经过 v 的路径
        for (int j = 1; j <= k; ++j)
        {
            dp[u][j] += dp[v][j - 1];
        }
    }
}
```

## 主函数

读入 n 个节点和 k 值，建树后从 1 号节点开始 DFS，输出长度为 k 的路径总数。

```cpp
int main()
{
    int n, k, a, b;

    while (scanf("%d %d", &n, &k) != EOF)
    {
        // 清空邻接表(多次输入时需要)
        for (int i = 1; i <= n; ++i)
        {
            tree[i].clear();
        }

        // 读入 n-1 条无向边,建树
        for (int i = 0; i < n - 1; ++i)
        {
            scanf("%d %d", &a, &b);
            tree[a].push_back(b);
            tree[b].push_back(a);
        }

        ans = 0;
        dfs(1, 0, k);
        printf("%lld\n", ans);
    }

    return 0;
}
```
