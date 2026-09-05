# count

## 算法思路

计数排序（桶排序）。

创建计数数组，统计每个数值出现的次数，然后按顺序输出。

适用于整数范围不大的情况。

```cpp
#define N 10
//桶排序/计数排序   (定义arry[数组里面最大的数字+1])
void countSort(int arr[],int length){
	int arry[100*length]={0};
	for(int i=0;i<length;i++){
		arry[arr[i]]++;
	}
	for(int i=0,j=0;i<100*length;i++){
		while(arry[i]--){
			arr[j++]=i;
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
        arr[i] = rand()%1000;
    }
    for(int i = 0;i<N;++i){
        cout << arr[i] << " ";
    }
    cout << endl;
    cout << endl;
    countSort(arr,N);
    for(int i = 0;i<N;++i){
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}
```
