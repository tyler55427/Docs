# bub（冒泡排序）

## 交换函数

```cpp
void swap(int arr[],int i,int j){
    int temp=arr[i];
    arr[i]=arr[j];
    arr[j]=temp;
}
```

## 冒泡排序

**说明**：如果中间出现排好序的情况后结束循环。i<length，第二个循环次数依次减少

```cpp
void bubSort(int arr[],int length){
    int flag=1;
    while(length--&&flag){
        //如果中间出现排好序的情况后结束循环 
        flag=0;
        //i<length，第二个循环次数依次减少 
        for(int i=0;i<length;i++){
            if(arr[i+1]<arr[i]){
                flag=1;
                swap(arr,i,i+1);
            }
        }
    }
}
```
