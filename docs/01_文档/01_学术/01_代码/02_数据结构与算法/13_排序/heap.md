# heap

## 算法思路

堆排序，包括外堆和内堆两种实现方式。

外堆使用额外的堆结构存储，内堆直接在原数组上进行堆化。

```cpp
void swap(int arr[],int i,int j){
	int temp=arr[i];
	arr[i]=arr[j];
	arr[j]=temp;
}
```

## 外堆实现

使用额外的数据结构（Heap结构体）存储堆。

```cpp
//堆排序(外堆)
typedef struct Heap{
	int *root;
	int length;
}Heap;
Heap* creatHeap(int length){
	Heap* heap=(Heap *)malloc(sizeof(Heap));
	assert(heap);
	heap->length=0;
	heap->root=(int*)malloc(sizeof(int)*length);
	assert(heap->root);
	return heap;
}
void pushHeap(Heap* heap,int data){
	int current=heap->length++;
	int parent=current/2;
	heap->root[current]=data;
	while(parent!=current){
		if(heap->root[current]<heap->root[parent]){
			swap(heap->root,current,parent);
			current=parent;
			parent=current/2;
		}
		else break;
	}
}


int popHeap(Heap *heap) {
	int val=heap->root[0];
	int current=0;
	int rchild=2*current+2;
	int small;
	heap->root[0]=heap->root[--heap->length];
	while(rchild<=heap->length){
		small=heap->root[rchild-1]<heap->root[rchild]?rchild-1:rchild;
		if(heap->root[small]<heap->root[current]){
			swap(heap->root,small,current);
			current=small;
			rchild=2*current+2;
		}
		else break;
	}
	return val;
}
void heapSort(int arr[],int length){
	Heap* heap=creatHeap(length);
	for(int i=0;i<length;i++){
		pushHeap(heap,arr[i]);
	}
	for(int i=0;i<length;i++){
		arr[i]=popHeap(heap);
	}
	free(heap->root);}
```

## 内堆实现

直接在原数组上进行堆化，然后逐步将堆顶元素移到数组末尾。

```cpp
//堆排序(内堆)
void heapify(int arr[],int length,int current){
	int rchild=2*current+2;
	int large;
	while(rchild<=length)
	{
		large=rchild==length?rchild-1:(arr[rchild-1]>arr[rchild]?rchild-1:rchild);
		if(arr[large]>arr[current]){
			swap(arr,large,current);
			current=large;
			rchild=2*current+2;
		}
		else break;
	}
}

void heapSort2(int arr[], int length){
	int current=length/2;
	while(current>=0){
		heapify(arr,length,current);
		current--;
	}
	while(length){
		swap(arr,0,--length);
		heapify(arr,length,0);

	}
}
```

## 课本实现

```cpp
// 课本
inline int leftChild(int i) {
	return 2 * i + 1;
}
void percDown(vector<int>& v, int i, int n) {
	int child;

	int temp = move(v[i]);
	for (;leftChild(i) < n;i = child) {
		child = leftChild(i);
		if (child != n - 1 && v[child] < v[child + 1]) {
			++child;
		}
		if (temp < v[child]) {
			v[i] = move(v[child]);
		}
		else
			break;
	}
	v[i] = move(temp);
}
void heap_Sort(vector<int>& v) {
	// buildHeap
	for (int i = v.size() / 2 - 1;i >= 0;--i) {
		percDown(v, i, v.size());
	}
	// deleteMax
	for (int j = v.size() - 1;j > 0;--j) {
		// 将最大的放到最后，节省空间
		swap(v[0], v[j]);
		percDown(v, 0, j);
	}
}
```
