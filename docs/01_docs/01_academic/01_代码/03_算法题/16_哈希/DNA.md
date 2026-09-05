# DNA

## 题目名称

**问题描述**：给定一个字符串 s 和 n 个查询，每个查询包含四个整数 a, b, c, d，判断 s[a..b] 与 s[c..d] 两个子串是否相同。

**解法**：使用滚动哈希（Rabin-Karp 风格）。预处理字符串的前缀哈希值和幂次，查询时通过公式 `(hash[l..r] = hash[r] - hash[l-1] * power[r-l+1]) % MOD` 计算区间哈希值并比较。模数 MOD = 19260817，基数 p = 19。

```cpp
#define MOD 19260817

long long ha[1000009];
long long power[1000009];

int main()
{
	int p=19;
	string s;
	cin>>s;
	power[0]=1;
	for(int i=0;i<s.length();++i)
	{
		ha[i+1]=(ha[i]*p+s[i]-'a'+1)%MOD;
		power[i+1]=(power[i]*p)%MOD;
	}
	int n;
	cin>>n;
	while(n--)
	{
		int a,b,c,d;
		cin>>a>>b>>c>>d;
		if((ha[b]-ha[a-1]*power[b-a+1]%MOD+MOD)%MOD
		 == (ha[d]-ha[c-1]*power[d-c+1]%MOD+MOD)%MOD ) cout<<"Yes"<<endl;
		else cout<<"No"<<endl;
	}
//	for(int i=1;i<=s.length();++i) cout<<ha[i]<<" ";
}
```

**备注**：

- 哈希冲突通过取模缓解，模数取大素数 19260817
