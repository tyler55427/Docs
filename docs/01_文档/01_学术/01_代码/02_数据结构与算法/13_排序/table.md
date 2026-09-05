# table

## 算法思路

表排序算法。

先生成排序索引表，再根据索引表交换元素得到排序结果。

```cpp

vector<int> Table_Sort(vector<int> &v){
	vector<int> t;
	int s=v.size();
	for(int i=0;i<s;++i) t.push_back(i);
	for(int i=1;i<s;++i){
		int temp=t[i];
		int j=i;
		for(;j&&v[temp]<v[t[j-1]];--j)
			t[j]=t[j-1];
		t[j]=temp;
	}
	return t;
}
```

## 表交换

```cpp
void Table_Swap(vector<int> &v,vector<int> &table){
	for(int i=0;i<v.size();++i){
		if(i!=table[i]){
			int c=v[i];
			int sign=i;
			while(i!=table[i]){
				if(table[i]==sign){
					v[i]=c;
					break;
				}
				v[i]=v[table[i]];
				int temp=i;
				i=table[i];
				table[temp]=temp;
			}
		}
	}
}
```

## 主函数

```cpp
int main(){
	vector<int> v={3,5,2,6,1,7,9};// 4 2 0 1 3 5 6
	vector<int> res=Table_Sort(v);
	for(auto &i:res) cout<<i<<" ";
	cout<<endl;
	Table_Swap(v,res);
	for(auto &i:v) cout<<i<<" ";
}
```
