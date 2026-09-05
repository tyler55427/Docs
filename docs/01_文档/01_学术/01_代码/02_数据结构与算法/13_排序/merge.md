# merge

## 递归实现

分治思想，将数组分成两半分别排序，然后合并。

```cpp

// 课本
void merge(vector<int>& v, vector<int>& tempArray, int leftPos, int rightPos, int rightEnd) {
    int leftEnd = rightPos - 1;
    int tempPos = leftPos;
    int numElements = rightEnd - leftPos + 1;

    while (leftPos <= leftEnd && rightPos <= rightEnd) {
        if (v[leftPos] <= v[rightPos])
            tempArray[tempPos++] = move(v[leftPos++]);
        else
            tempArray[tempPos++] = move(v[rightPos++]);
    }

    while (leftPos <= leftEnd)
        tempArray[tempPos++] = move(v[leftPos++]);
    while (rightPos <= rightEnd)
        tempArray[tempPos++] = move(v[rightPos++]);

    for (int i = 0;i < numElements;++i, --rightEnd)
        v[rightEnd] = move(tempArray[rightEnd]);

}

void mergeSort(vector<int>& v, vector<int>& tempArray, int left, int right) {
    if (left < right) {
        int center = (left + right) / 2;
        mergeSort(v, tempArray, left, center);
        mergeSort(v, tempArray, center + 1, right);
        merge(v, tempArray, left, center + 1, right);
    }
}

void mergeSort(vector<int>& v) {
    vector<int> tempArray(v.size());
    mergeSort(v, tempArray, 0, v.size() - 1);
}
```

## 非递归实现

自底向上，先两两合并，然后四四合并，逐步扩大跨度直到整个数组。

```cpp
// 非递归实现
void merge(int arr[],int temp[],int left,int mid,int right){
	int l=left,m=mid-1,r=mid;
	int t=left;
	while(l<=m&&r<=right){
		if(arr[l]<=arr[r]) temp[t++]=arr[l++];
		else temp[t++]=arr[r++];
	}
	while(l<=m) temp[t++]=arr[l++];
	while(r<=right) temp[t++]=arr[r++];
	for(int k=left;k<=right;++k) arr[k]=temp[k];
}

void merge(int arr[],int temp[],int N,int length){
	int i=0;
	for(;i<=N-2*length;i+=2*length)
		merge(arr,temp,i,i+length,i+2*length-1);

	if(i+length<N) merge(arr,temp,i,i+length,N-1);
	else
	for(int j=i;j<N;++j) arr[j]=temp[j];
}

void merge_sort(int arr[],int temp[],int N){
	int length=1;
	while(length<N){
		merge(arr,temp,N,length);
		length*=2;
	}
}
```
