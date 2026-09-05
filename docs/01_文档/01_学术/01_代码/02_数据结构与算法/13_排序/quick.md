# quick

## 快速排序递归版

找到轴pivot使左边都小，右边都大。数据杂乱无章，越乱越快。

```cpp

//快速排序(递归)(找到轴povid使左边都小,右边都大)(数据杂乱无章，越乱越快)
void quickSort(int arr[],int left,int right){
	if (left >= right)return;
	int i = left, j = right;
	int pivot = arr[i];
	while (i < j) {
		while (i < j && arr[j] >= pivot)
			j--;
		arr[i] = arr[j];
		while (i < j && arr[i] <= pivot)
			i++;
		arr[j] = arr[i];
	}
	arr[i]=pivot;
	quickSort(arr,left,i-1);
	quickSort(arr,i+1,right);
}
```

## 快速排序单链表版

```cpp
//快速排序(单链表)
void quickSortI(int arr[],int left,int right){
	if(left>=right)return;
	int pivot=arr[left];
	int i=left+1,j=left+1;
	while(j<=right){
		if(arr[j]<pivot){
			int temp=arr[i];
			arr[i]=arr[j];
			arr[j]=temp;
			i++;
		}
		j++;
	}
	int temp=arr[left];
	arr[left]=arr[i-1];
	arr[i-1]=temp;
	quickSortI(arr,left,i-2);
	quickSortI(arr,i,right);
}
```

## 课本实现

使用三数取中法选择枢轴，并设置阈值10，当子数组小于10时使用插入排序。

```cpp
// 课本
const int& median3(vector<int>& v, int left, int right) {
	int center = (left + right) / 2;

	if (v[center] < v[left])
		swap(v[center], v[left]);
	if (v[right] < v[left])
		swap(v[right], v[left]);
	if (v[right] < v[center])
		swap(v[center], v[right]);
	// 轴不能在数组中间，否则不一定能够满足轴要求的性质
	swap(v[center], v[right - 1]);
	return v[right - 1];
}
// 插入排序（课本）
void insertionSort(vector<int>& v,int left,int right) {
    for (int p = left;p <= right;++p) {
        int temp = move(v[p]);

		int j = p;
		// 通过短路保证不会越界
		for (;j > 0 && temp < v[j - 1];--j) {
            v[j] = move(v[j - 1]);
        }
        v[j] = move(temp);
    }
}
void quick_sort(vector<int>& v, int left, int right) {
	if (left + 10 <= right) {
		const int& pivot = median3(v, left, right);

		// 为什么上面排序了还要？下面解释
		int i = left, j = right - 1;
		while (true) {
			// 细节，不管怎样都要进行++、--，这个也是不陷入死循环的关键
			// 死循环哪来的呢？遇到相同的，停下来交换，如果++、--在后面，就一直进入交换的那两个数？
			while (v[++i] < pivot) {}
			while (pivot < v[--j]) {}
			if (i < j)
				swap(v[i], v[j]);
			else
				break;
		}
		swap(v[i], v[right - 1]);

		quick_sort(v, left, i - 1);
		quick_sort(v, i + 1, right);
	}
	else
		insertionSort(v, left, right);
}
void quick_sort(vector<int>& v) {
	quick_sort(v, 0, v.size() - 1);
}
```
