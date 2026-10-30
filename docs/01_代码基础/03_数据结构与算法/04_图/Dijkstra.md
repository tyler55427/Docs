# Dijkstra

## Dijkstra 算法

**说明**：使用优先队列实现的 Dijkstra 最短路径算法

```cpp
void Dijkstra(int x) {
    for(int i=1;i<=100000;++i){
        nnode[i].d=0x7fffffff;
    }
    q.push({ x,0 });
    nnode[x].d=0;
    while (!q.empty()) {
        int now=q.top().v;
        q.pop();
        if(!sign[now]){
            sign[now]=true;
            for(auto &i:nnode[now].adj){
                if(!sign[i.v]){
                    if(nnode[now].d+i.val<nnode[i.v].d){
                        nnode[i.v].d=nnode[now].d+i.val;
                        nnode[i.v].back = now;
                        // 只有更新了才入队
                        q.push({ i.v,nnode[i.v].d });
                    }
                    // 和Prim区别，Prim是点到集合的最短距离，Dijkstra是点到点的最短距离
					// else if (nnode[now].d + i.val == nnode[i.v].d&&
					// 	cost[now] + cost < cost[i.v]) {
					// 	cost[i.v] = cost[now] + cost;
					// }
                }
            }
        }
    }
}
```

## 主函数

**说明**：读取图数据并输出从 s 到各点的最短距离

```cpp
int main() {
    // 输入为节点数n，边数m，和从s节点开始
    int n, m, s;
    cin>>n>>m>>s;
    int x,y,z;
    for(int i=0;i<m;++i){
        cin>>x>>y>>z;
        nnode[x].adj.push_back({y,z});
    }
    Dijkstra(s);
    for (int i = 1;i <= n;++i) {
        if(nnode[i].d!=0x7fffffff) cout<<nnode[i].d<<" ";
        else cout<<"-1 ";
    }
}
```
