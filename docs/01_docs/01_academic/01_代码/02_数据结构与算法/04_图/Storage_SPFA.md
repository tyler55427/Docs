# Storage_SPFA

## 算法思路

使用SPFA算法求单源最短路径，同时统计最短路径的条数。

SPFA是Bellman-Ford的队列优化版本，不断从队列中取出节点进行松弛操作。

```cpp

#define N 4000009
int to[N],head[N],nxt[N],d[N],res[N];
bool vis[N];
int cnt;
queue<int> q;

void add(int x,int y){
	to[++cnt]=y;
	nxt[cnt]=head[x];
	head[x]=cnt;
}

int main(){
	ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
	int n,m;
	cin>>n>>m;
	int x,y;
	for(int i=0;i<m;++i){
		cin>>x>>y;
		add(x,y);
		add(y,x);
	}
	for(int i=1;i<=n;++i) d[i]=1e7;
	d[1]=0;
	res[1]=1;
	vis[1]=1;
	q.push(1);
	while(!q.empty()){
		x=q.front();
		q.pop();
		vis[x]=0;
		for(int i=head[x];i;i=nxt[i]){
			y=to[i];
			if(d[y]>d[x]+1){
				d[y]=d[x]+1;
				res[y]=res[x];
				if(!vis[y]){
					vis[y]=1;
					q.push(y);
				}
			}
			else if(d[y]==d[x]+1){
				res[y]=(res[y]+res[x])%100003;
			}
		}
	}
	for(int i=1;i<=n;++i) cout<<res[i]<<endl;
	return 0;
}
```
