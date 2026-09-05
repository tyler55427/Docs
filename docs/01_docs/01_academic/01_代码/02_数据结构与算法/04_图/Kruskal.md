# Kruskal（最小生成树）

## 并查集

**说明**：查找根节点，使用路径压缩

```cpp
int find(int x) {
    // 如果不是根节点，就一直往上找
    if (sset[x] != x)
        // 这里是路径压缩，将x的父节点设为x的根节点
        sset[x] = find(sset[x]);
    return sset[x];
}
```

**说明**：合并两个集合

```cpp
void unio(int x, int y) {
    // 注意两个都要find，找到最上层的根节点
    sset[find(x)] = find(y);
}
```

## Kruskal 算法

**说明**：使用优先队列，边从小到大处理，如果两个节点不在同一个集合中，就合并

```cpp
void Kruskal() {
    while (!q.empty()) {
        node temp = q.top();
        q.pop();
        // 如果两个节点不在同一个集合中，就合并
        if (find(temp.v1) != find(temp.v2)) {
            cout << temp.val << " " << temp.v1 << " " << temp.v2 << endl;
            unio(temp.v1, temp.v2);
            res += temp.val;
        }
    }
}
```

## 主函数

```cpp
int main() {
    int n;
    cin >> n;
    for (int i = 0;i < n;++i) {
        sset[i + 1] = i + 1;
        for (int j = 0;j < n;++j) {
            cin >> arr[i][j];
            if (arr[i][j]) {
                q.push({ arr[i][j],i,j });
            }
        }
    }

    Kruskal();
    cout << res << endl;
}
```
