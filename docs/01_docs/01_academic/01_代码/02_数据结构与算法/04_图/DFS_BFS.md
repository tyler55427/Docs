# DFS_BFS

## 深度优先搜索 (DFS)

```cpp
void dfs(int i)
{    
    cout<<i<<" ";
    sign[i]=true;

    for(int j=0;j<v[i].size();++j)
    {
        if(!sign[v[i][j]])
            dfs(v[i][j]);
    }
}
```

## 广度优先搜索 (BFS)

```cpp
void bfs(int i)
{
    q.push(1);
    while(!q.empty())
    {
        int temp=q.front();
        q.pop();
        if(!sign[temp])
        {    
            sign[temp]=true;
            cout<<temp<<" ";
        }
        for(int j=0;j<v[temp].size();++j)
        {
            if(!sign[v[temp][j]])
            {
                q.push(v[temp][j]);
            }
        }
    }
}
```

## 主函数

**说明**：读取节点数 n 和边数 m，构建图并输出 DFS 和 BFS 结果

```cpp
int main()
{
    int n,m;
    cin>>n>>m;
    int a,b;
    for(int i=0;i<m;++i)
    {
        cin>>a>>b;
        v[a].push_back(b);
    }
    for (int i = 1; i <= n; ++i) 
    {
        sort(v[i].begin(), v[i].end());
    }
    dfs(1);
    cout<<endl;
    for(int i=0;i<=n;++i)
    {
        sign[i]=false;
    }
    bfs(1);
}
```
