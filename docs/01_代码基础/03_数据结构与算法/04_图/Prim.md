# Prim（最小生成树）

## Prim 算法

**说明**：边结构体，记录边的起点、终点和权重

```cpp
struct Edge {
    int from, to;
    int weight;
    Edge(int from = 0, int to = 0, int weight = 0)
        : from(from), to(to), weight(weight) {}
};
```

**说明**：从起点 start 开始，使用队列实现朴素 Prim

```cpp
void Prim(int start) {
    // 从起点 start 开始，初始边视为 (start, start, 0)
    edge_queue.push({start, start, 0});

    while (!edge_queue.empty()) {
        Edge current = edge_queue.front();
        edge_queue.pop();

        // 如果终点未访问，则加入 MST
        if (!visited[current.to]) {
            visited[current.to] = 1;  // 标记已访问

            // 输出当前选取的边
            cout << current.from << " " << current.to << " " << current.weight << endl;
            total_weight += current.weight;

            // 遍历当前顶点的所有邻接边
            for (const auto& edge : graph[current.to]) {
                if (!visited[edge.to]) {
                    edge_queue.push(edge);
                }
            }
        }
    }
}
```

## 主函数

```cpp
int main() {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    // n: 顶点数, m: 边数
    int n, m;
    cin >> n >> m;

    // 读入 m 条无向边
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back({u, v, w});
        graph[v].push_back({v, u, w});
    }

    cout << endl;
    Prim(1);  // 从顶点 1 开始构建 MST
    cout << total_weight << endl;

    return 0;
}
```
