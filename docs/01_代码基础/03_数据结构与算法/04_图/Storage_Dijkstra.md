# Storage_Dijkstra

## 算法思路

使用Dijkstra算法求单源最短路径。

使用优先队列（最小堆）实现，从源点开始，每次选择距离最小的未访问节点进行松弛操作。

```cpp
#define M(x,y) make_pair(x,y)

#define N 400009
int to[N],head[N],nxt[N],d[N],w[N];
bool vis[N];
int cnt;
priority_queue<pair<int,int>> q;

void add(int x,int y,int val){
	to[++cnt]=y;
	w[cnt]=val;
	nxt[cnt]=head[x];
	head[x]=cnt;
}

int main(){
	ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
	int n,m,s;
	cin>>n>>m>>s;
	int x,y,val;
	for(int i=0;i<m;++i){
		cin>>x>>y>>val;
		add(x,y,val);
	}
	for(int i=1;i<=n;++i) d[i]=1e10;
	d[s]=0;
	q.push(M(0,s));
	while(!q.empty()){
		x=q.top().second;
		q.pop();
		if(!vis[x]){
			vis[x]=1;
			for(int i=head[x];i;i=nxt[i]){
				y=to[i];
				if(d[y]>d[x]+w[i]){
					d[y]=d[x]+w[i];
					q.push(M(-d[y],y));
				}
			}
		}
	}
	for(int i=1;i<=n;++i) cout<<d[i]<<" ";
	return 0;
}
```
