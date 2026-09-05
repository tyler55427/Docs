# redix

## 算法思路

基数排序。

按位数从低到高进行桶分配，先按个位分配，再按十位分配，以此类推，直到最高位。

```cpp

void redix_Sort(vector<int>& v) {
	int maxv=0,n=0;
	for (auto& i : v) {
		maxv = max(maxv, i);
	}
	while (maxv) {
		maxv / 10;
		n++;
	}
	for (int k = 0;k < n;++k) {
		vector<vector<int>> temp(10);
		for (auto& i : v) {
			int t = pow(10, n);
			temp[(i / t) % 10].push_back(i);
		}
		v.clear();
		for (auto& i : temp) {
			for (auto& j : i) {
				v.push_back(j);
			}
		}
		temp.clear();
	}
}
```

## 主函数

```cpp
int main() {
	srand((unsigned)time(NULL));
	vector<int> v;
	for (int i = 0;i < 1000;++i) {
		v.push_back(rand() % 1000);
	}
	for (auto& i : v)
		cout << i << " ";
	cout << endl;
	redix_Sort(v);
	for (auto& i : v)
		cout << i << " ";
	cout << endl;

}
```
