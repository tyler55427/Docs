# Floyd

## 算法思路

求图中任意两点间的最短路径（传递闭包）。Floyd算法使用动态规划思想，枚举中间节点k，更新i到j的最短距离。

```cpp

int g[109][109];
int n,m;

// 传递闭包
int main() {
	cin>>n>>m;
	int u,v,w;
	for(int i=1;i<=n;++i){
		for(int j=1;j<=n;++j){
			if(i!=j) g[i][j]=1e9;
		}
	}
	for(int i=0;i<m;++i){
		cin>>u>>v>>w;
		g[u][v]=min(g[u][v],w);
		g[v][u]=min(g[v][u],w);
	}
	for(int k=1;k<=n;++k){
		for(int i=1;i<=n;++i){
			for(int j=1;j<=n;++j){
				g[i][j]=min(g[i][j],g[i][k]+g[k][j]);
			}
		}
	}
	for(int i=1;i<=n;++i){
		for(int j=1;j<=n;++j){
			cout<<g[i][j]<<" ";
		}
		cout<<endl;
	}
	return 0;
}
```
