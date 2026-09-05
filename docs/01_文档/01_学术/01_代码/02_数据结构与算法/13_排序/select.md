# select

## 算法思路

选择排序。

每趟从未排序序列中选出最小元素，放到已排序序列的末尾。

简单选择排序使用双层循环，时间复杂度O(n^2)。

```cpp
#define N 100
void swap(int arr[],int i,int j){
	int temp=arr[i];
	arr[i]=arr[j];
	arr[j]=temp;
}
//选择排序 (三指针)
void selectSort(int arr[],int length){
	int i,j,k;
	for (i=0;i<length;i++){
		k=i;
		for(j=i+1;j<length;j++){
			if(arr[j]<arr[k]){
				k=j;
			}}
			if(k!=i){
			swap(arr,k,i);
		}
	}
}
//简单的思路？
void selectSort_(int arr[],int length){
    for (int i = 0;i < length;i++) {
        for (int j = i;j < length;j++) {
            if (arr[i] > arr[j])
                swap(arr[i], arr[j]);
        }
    }
}
```

## 主函数

```cpp
int main(){
    srand ((unsigned) time(NULL));
    int arr[N];
    for(int i = 0;i<N;++i){
        arr[i] = rand()%100;
    }
    for(int i = 0;i<N;++i){
        cout << arr[i] << " ";
    }
    cout << endl;
    selectSort_(arr,N);
    for(int i = 0;i<N;++i){
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}
```
