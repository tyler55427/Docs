# insert_shell

## 插入排序

对于每个元素，找到它在已排序序列中的正确位置并插入。在有一定顺序上，往后找不符合顺序的往前放。

```cpp
void swap(int arr[],int i,int j){
	int temp=arr[i];
	arr[i]=arr[j];
	arr[j]=temp;
}
//插入排序(在有一定顺序上，往后找不符合顺序的往前放)
void insertSort(int arr[],int length){
	int i,j;
	for(i=1;i<length;i++){
		for(j=i;j>=1&&arr[j]<arr[j-1];j--){
			swap(arr,j-1,j);
		}
	}
}
```

## 希尔排序

插入排序的改进版，使用增量序列分组，先大跨度比较，逐步缩小增量直到1。步幅大的插入排序，最后变成插入排序，适合很大的数组。

```cpp
//希尔排序(步幅大的插入排序，最后变成插入排序，适合很大的数组)
void shellSort(int arr[],int length){
	int h=1,i,j;
	int t=length/3;
	while(h<t)
	h=3*h+1;
	while(h>=1){
		for(i=h;i<length;i++){
		    for(j=i;j>=h&&arr[j]<arr[j-1];j-=h){
                swap(arr, j, j - h);
            }
	    }
		h/=3;
	}
}
```

## 课本实现

```cpp
// 插入排序（课本）
void insertionSort(vector<int>& v) {
    for (int p = 1;p < v.size();++p) {
        int temp = move(v[p]);

        int j = p;
        for (;j > 0 && temp < v[j - 1];--j) {
            v[j] = move(v[j - 1]);
        }
        v[j] = move(temp);
    }
}
// 希尔排序（课本）
void shellsort(vector<int> &v) {
    for (int gap = v.size() / 2;gap > 0;gap /= 2) {
        for (int i = gap;i < v.size();++i) {
            int temp = move(v[i]);

            int j = i;
            for (;j >= gap && temp < v[j - gap];j -= gap) {
                v[j] = move(v[j - gap]);
            }
            v[j] = move(temp);
        }
    }
}
```
