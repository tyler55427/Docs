# Vital_Route

## 算法思路

求工程项目的关键路径。

计算每个活动的最早完成时间和最晚完成时间。

使用拓扑排序的思想，正向传播计算最早完成时间，逆向传播计算最晚完成时间。

```cpp

#define N 10009
vector<int> v1[N],v2[N];
queue<int> q;
int val[N], inque[N];
int ee[N], le[N],e[N],l[N];
int n,FirstTime;
```

## 最早完成时间

```cpp
// 最早完成时间
void EarFini() {
    for(int i=1;i<=n;++i){
		if(v2[i].empty()){
			ee[i]=val[i];
			q.push(i);
			inque[i]=1;
		}
	}
	while(q.size()){
		int now=q.front();
		q.pop();
		inque[now]=0;
		for(auto &i:v1[now]){
			if(ee[i]<ee[now]+val[i]){
				ee[i]=ee[now]+val[i];
				q.push(i);
				inque[i]=1;
			}
		}
	}
	for(int i=1;i<=n;++i){
		if(v1[i].empty()){
			FirstTime=max(FirstTime,ee[i]);
		}
    }

    cout << "FirstTime: " << FirstTime << endl;

    memset(inque, 0, sizeof(inque));

}
```

## 最晚完成时间

```cpp
// 最晚完成时间
void LaFini() {
	for (int i = 1;i <= n;++i) le[i] = 0x3f3f3f;
	for (int i = 1;i <= n;++i) {
        if (v1[i].empty()) {
            le[i] = FirstTime;
            q.push(i);
            inque[i] = 1;
        }
    }

    while (q.size()) {
        int now = q.front();
        q.pop();
        inque[now] = 0;
        for (auto& i : v2[now]) {
            if (le[i] > le[now] - val[now]) {
                le[i] = le[now] - val[now];
                q.push(i);
                inque[i] = 1;
            }
        }
    }
}
```

## 主函数

```cpp
int main(){
	cin>>n;
	int vv,id;
	for(int i=1;i<=n;++i){
		cin>>id>>val[i];
		while(cin>>vv&&vv){
            v1[vv].push_back(i);
            v2[i].push_back(vv);
        }
	}

    EarFini();
	LaFini();
	for (int i = 1;i <= n;++i) cout << i << ": " << ee[i] << endl;
	cout << endl;
	for (int i = 1;i <= n;++i) cout << i << ": " << le[i] << endl;
	cout << endl;
	return 0;
}
```
