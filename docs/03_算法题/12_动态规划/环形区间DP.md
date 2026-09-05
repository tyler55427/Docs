# 环形区间DP

## 题目名称

**问题描述**：将环形的 n 堆石子合并成一堆，合并代价为两堆石子数量之和，求最小和最大合并代价。

**解法**：区间 DP。先将数组复制扩展，用 dp_min[i][j] 和 dp_max[i][j] 表示区间 [i, j] 的最小和最大合并代价。枚举分割点 k 进行状态转移。最后取所有长度为 n 的区间的最小/最大值。

```cpp
int n;
int arr[10005], sum[10005];
int dp_min[10005][10005], dp_max[10005][10005];


// 区间DP合并问题，环
int main() {
	cin >> n;
	for (int i = 0;i < n;++i) {
		cin >> arr[i];
		sum[i + 1] = sum[i] + arr[i];
	}
	for (int i = 0;i < n;++i) {
		arr[i + n] = arr[i];
		sum[i + n + 1] = sum[i + n] + arr[i + n];
	}
	for (int len = 2;len <= n;++len) {
		for (int i = 0;i + len - 1 < 2*n;++i) {
			int j = i + len - 1;
			dp_min[i][j] = 1e9;
			dp_max[i][j] = -1e9;
			for (int k = i;k < j;++k) {
				dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j] + sum[j + 1] - sum[i]);
				dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j] + sum[j + 1] - sum[i]);
			}
		}
	}
	int ans_min = 1e9, ans_max = -1e9;
	for (int i = 0;i < n;++i) {
		ans_min = min(ans_min, dp_min[i][i + n - 1]);
		ans_max = max(ans_max, dp_max[i][i + n - 1]);
	}
	cout << ans_min << " " << ans_max << endl;
}
```
