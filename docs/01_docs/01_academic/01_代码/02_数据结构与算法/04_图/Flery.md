# Flery

## 算法思路

判断给定有向图是否存在欧拉回路，若存在则输出一条欧拉回路。

使用Fleury算法，首先检查图中每个节点的入度和出度之差是否满足条件。

```cpp

#define N 100009
#define M 200009

vector<int> ver[N];
int din[N], dout[N],del[M];
stack<int> q;

// 欧拉回路

// 似乎没有，都是dfs
// 连通性，并查集 或 dfs

void dfs(int now)
{
	for(int i=del[now];i<ver[now].size();i=del[now])
	{
		del[now]=i+1;
		dfs(ver[now][i]);
	}
	q.push(now);
}
```

## 主函数

```cpp
int main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int n, m;
    cin >> n >> m;
    int u, v;
    for (int i = 0;i < m;++i) {
        cin >> u >> v;
        ver[u].push_back(v);
        dout[u]++;
        din[v]++;
    }
    for (int i = 1;i <= n;++i) sort(ver[i].begin(), ver[i].end());
    int start = 0, end = 0;
    int begin = 1;
    for (int i = 1;i <= n;++i) {
        if (din[i] - dout[i] > 1 || dout[i] - din[i] > 1) {
            cout << "No\n";
            return 0;
        }
        if (din[i] == dout[i] + 1) {
            end++;
        }
        else if (dout[i] == din[i] + 1) {
            begin = i;
            start++;
        }
    }
    if ((start == 0 && end == 0) || (start == 1 && end == 1)) {
        dfs(begin);
        while (q.size()) {
            cout << q.top() << " ";
            q.pop();
        }
    }
    else {
        cout << "No\n";
    }
    return 0;
}
```
