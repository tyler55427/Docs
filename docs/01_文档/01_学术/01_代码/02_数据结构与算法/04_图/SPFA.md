# SPFA

## SPFA 算法

**说明**：Shortest Path Faster Algorithm，用于单源最短路径

```cpp
void SPFA(ll x){
    for(ll i=1;i<=n;++i){
        nnode[i].d=1e18;
    }
    nnode[x].d=0;
    q.push({x,0});
    while(!q.empty()){
        dis temp=q.front();
        q.pop();
        nnode[temp.v].sign=false;
        for(auto &i:nnode[temp.v].adj){
            if(nnode[temp.v].d+i.val<nnode[i.v].d){
                nnode[i.v].d=nnode[temp.v].d+i.val;
                if(!nnode[i.v].sign){
                    q.push({i.v,nnode[i.v].d});
                    nnode[i.v].sign=true;
                }
            }
        }
    }
}
```

## 主函数

```cpp
int main(){
    cin>>n>>m;
    ll x,y,z;
    for(ll i=0;i<m;++i){
        cin>>x>>y>>z;
        nnode[x].adj.push_back({y,z});
    }
    SPFA(1);
    for(ll i=1;i<=n;++i){
        if(nnode[i].d!=1e18) cout<<nnode[i].d<<" ";
        else cout<<"-1 ";
    }
    return 0;
}
```
