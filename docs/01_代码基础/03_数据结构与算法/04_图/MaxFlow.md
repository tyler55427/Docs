# MaxFlow

## 算法思路

求给定网络图的最大流。

使用Edmonds-Karp算法（基于BFS的增广路径算法），每次BFS找到一条增广路径，更新残余网络，累加流量直到不存在增广路径。

```cpp

typedef long long ll;

ll n, m, start, goal, u, v, w;
ll cal[209][209],d[209],from[209],res[209][209];
queue<ll> q;
stack<ll> st;

ll Maxflow() {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    ll flow = 0;
    while (true) {
        memset(d, 0, sizeof(d));
        memset(from, 0, sizeof(from));
        while(q.size()) q.pop();
        q.push(start);
        d[start] = 0x3f3f3f3f3f3f3f3f;
        while (q.size()) {
            ll now = q.front();
            q.pop();
            for (ll i = 1;i <= n;++i) {
                if (d[i] == 0 && (cal[now][i] != 0)) {
                    if (cal[now][i] > 0) {
                        d[i] = min(d[now], cal[now][i]);
                    }
                    else {
                        d[i] = min(d[now], -cal[now][i]);
                    }
                    from[i] = now;
                    q.push(i);
                }
            }
            if (d[goal]) break;
        }
        if (d[goal] == 0) break;
        for (ll i = from[goal], k = goal;i;k = i, i = from[i]) {
            if (i == from[goal]) st.push(goal);
            st.push(i);
            if (cal[i][k] > 0) {
                res[i][k] += d[goal];
                cal[i][k] -= d[goal];
                cal[k][i] -= d[goal];
            }
            else if (cal[i][k] < 0) {
                res[i][k] -= d[goal];
                cal[i][k] += d[goal];
                cal[k][i] += d[goal];
            }
        }
        while (st.size()) {
            cout << st.top() << " ";
            st.pop();
        }
        cout << "val: " << d[goal] << endl;
        flow += d[goal];
    }
    return flow;
}
```

## 主函数

```cpp
int main() {
    cin >> n >> m >> start >> goal;
    for (int i = 0;i < m;++i) {
        cin >> u >> v >> w;
        cal[u][v] += w;
    }
    cout << Maxflow() << endl;
    return 0;
}
```
