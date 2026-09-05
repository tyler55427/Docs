# Six_Degrees

## 算法思路

六度空间理论验证，使用BFS遍历图并统计在六度内能访问到的节点数。

使用BFS层次遍历，记录每层的节点，当遍历到第六层时停止。

```cpp

#define N 1009
queue<int> q;
vector<int> ver[N];
bool vis[N];

int bfs(int x) {
    vis[x] = 1;
    int level = 0, last = x, tail = 0, now = 0, count = 1;
    q.push(x);
    while (q.size()) {
        now = q.front();
        q.pop();
        for (auto& i : ver[now]) {
            if (!vis[i]) {
                vis[i] = 1;
                q.push(i);
                tail = i;
            }
        }
        if (now == last) {
            level++;
            last = tail;
        }
        if (count == 6) break;
    }
    return count;
}
```
