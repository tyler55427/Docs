# 图 m 着色

## 图 m 着色（Graph M-Coloring）

**问题描述**：给定一个无向图和 m 种颜色，求将图的每个顶点着色，使得相邻顶点颜色不同的方案数。

**解法**：回溯法（DFS）。对每个顶点依次尝试每种颜色，用 check 函数判断当前颜色是否与相邻顶点冲突。

```cpp
bool g[109][109];
int color[109];
int n,k,m,res;

bool check(int x){
	for(int i=1;i<=x;++i){
		if(g[x][i]&&color[i]==color[x]) return false;
	}
	return true;
}

void dfs(int x){
	if(x>n){
		res++;
		return;
	}
	for(int i=1;i<=m;++i){
		color[x]=i;
		if(check(x)){
			dfs(x+1);
		}
		else{
			color[x]=0;
		}
	}
}

int main(){
	cin>>n>>k>>m;
	int u,v;
	for(int i=0;i<k;++i){
		cin>>u>>v;
		g[u][v]=g[v][u]=1;
	}
	dfs(1);
	cout<<res;
}
```

**备注**：

- n：顶点数，k：边数，m：颜色数
- res 累计所有合法的着色方案数
- 回溯法适合 m 较小的情况，时间复杂度指数级
