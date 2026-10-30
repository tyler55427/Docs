# Maxflow_discrete

## 算法思路

离散最大流问题，将图中的节点离散化（索引+1），添加超级源点和超级汇点，求最大流。

与MaxFlow类似，代码中自动为没有入边的节点连接超级源点（容量1000），为没有出边的节点连接超级汇点（容量1000）。

```cpp

int n, m, u, v, w;
int cal[209][209], d[209], from[209], res[209][209], ceng[209];
bool ru[209], chu[209];
queue<int> q;
stack<int> st;
vector<int> ver;

void bfs(int s){
    q.push(s);
    while (q.size()) {
        int now = q.front();
        q.pop();
        for (int i = 1;i <= n+2 ;++i) {
            if (cal[now][i]&&from[i]==0) {
                from[i] = 1;
                q.push(i);
                ceng[i] = ceng[now] + 1;
            }
        }
    }
}
```

## 最大流函数

```cpp
int Maxflow(int ss,int ee) {
    int flow = 0;
    while (true) {
        memset(d, 0, sizeof(d));
        memset(from, 0, sizeof(from));
        ver.clear();
        ver.push_back(ss);
        d[ss] = 0x3f3f3f;
        while(ver.size()) {
            int now = ver[0];
            ver.erase(ver.begin());
            for (int i = 1;i <= ee;++i) {
                if (d[i] == 0 && (cal[now][i] != 0)) {
                    if (cal[now][i] > 0) {
                        d[i] = min(d[now], cal[now][i]);
                    }
                    else {
                        d[i] = min(d[now], -cal[now][i]);
                    }
                    from[i] = now;
                    ver.push_back(i);
                     for (int k = ver.size() - 1;k >= 1;--k) {
                         if (ceng[ver[k]] < ceng[ver[k - 1]]) {
                             swap(ver[k], ver[k - 1]);
                         }
                         else if (ceng[ver[k]] == ceng[ver[k - 1]] && ver[k] < ver[k - 1]) {
                             swap(ver[k], ver[k - 1]);
                         }
                     }
                }
            }
            if (d[ee]) break;
        }
        if (d[ee] == 0) break;
        for (int i = from[ee], k = ee;i;k = i, i = from[i]) {
            st.push(i);
            if (cal[i][k] > 0) {
                res[i][k] += d[ee];
                cal[i][k] -= d[ee];
                cal[k][i] -= d[ee];
            }
            else if (cal[i][k] < 0) {
                res[i][k] -= d[ee];
                cal[i][k] += d[ee];
                cal[k][i] += d[ee];
            }
        }
        while (st.size()) {
            if(st.top()!=1) cout << st.top() - 1 << " ";
            st.pop();
        }
        cout << "val: " << d[ee] << endl;
        flow += d[ee];
    }
    return flow;
}
```

## 主函数

```cpp
int main() {
    cin >> n >> m;
    for (int i = 0;i < m;++i) {
        cin >> u >> v >> w;
        cal[u + 1][v + 1] += w;
        chu[u] = 1;
        ru[v] = 1;
    }
    for (int i = 1;i <= n;++i) {
        if (!ru[i])
            cal[1][i + 1] += 1000;
        if (!chu[i])
            cal[i + 1][n + 2] += 1000;
    }
    bfs(1);
    cout << Maxflow(1, n + 2) << endl;
    return 0;
}
```
