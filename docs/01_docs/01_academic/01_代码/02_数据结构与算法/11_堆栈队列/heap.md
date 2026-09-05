# heap

## 结构定义

使用数组模拟堆，支持大顶堆或小顶堆。完全二叉树的顺序存储，通过sign参数控制堆类型。

```cpp
typedef struct Heap
{
	int* p;
	int size, capacity;
	bool sign;
	Heap(int capa, bool sign = false) :p(nullptr), size(0), capacity(capa), sign(sign) {}
}heap;
```

## 堆的构建与销毁

```cpp
heap* build(bool op, int capa = 100)
{
	heap* t = new heap(capa, op);
	t->p = new int[capa + 1];
	t->p[0] = op ? -10 : 0x3f4f4f4f;
	return t;
}

void clear(heap*& h)
{
	if (h == nullptr) return;
	delete[] h->p;
	delete h;
	h = nullptr;
}

heap* extend(heap* h)
{
	heap* temp = new heap(2 * h->capacity, h->sign);
	temp->p = new int[temp->capacity];
	temp->size = h->size;
	for (int i = 1;i <= h->size;++i)
	{
		temp->p[i] = h->p[i];
	}
	clear(h);
	return temp;
}
```

## 向下调整

```cpp
void down(heap*& h, int x = 1)
{
	if (h->size == 1) return;
	int k;
	int temp = h->p[x];
	while (x * 2 <= h->size)
	{
		k = 2 * x;
		if (k != h->size && (h->p[k] < h->p[k + 1] ^ h->sign)) k++;
		if (h->p[k] > temp ^ h->sign)
		{
			h->p[x] = h->p[k];
		}
		else break;
		x = k;
	}
	h->p[x] = temp;
}
```

## 插入与弹出

```cpp
void insert(heap*& h, int x)
{
	if (h->size + 1 > h->capacity) h = extend(h);
	h->size++;
	h->p[h->size] = x;
	int k = h->size;
	while (k && (h->p[k] > h->p[k / 2] ^ h->sign))
	{
		swap(h->p[k], h->p[k / 2]);
		k /= 2;
	}
}

void pop(heap*& h)
{
	if (h->size == 0)
	{
		cout << "!!!Empty!!!" << endl;
		return;
	}
	h->p[1] = h->p[h->size--];
	down(h);
}

void top(heap* h)
{
	if (h->size == 0)
	{
		cout << "!!!Empty!!!" << endl;
		return;
	}
	cout << "The top val is: " << h->p[1] << endl;
}
```

## 主函数

```cpp
int main()
{
	int s;
	cout << "0 is max_root_heap or 1 is min_root_heap" << endl;
	cin >> s;
	char c;
	heap* h = build(s);
	while (true)
	{
		cout << endl;
		cout << "Insert 'i' and a number" << endl;
		cout << "Pop 'p'" << endl;
		cout << "Top 't' to show the top val" << endl;
		cout << "Clear 'd'" << endl;
		cin >> c;
		int val;
		if (c == '#') break;
		else if (c == 'i')
		{
			cin >> val;
			insert(h, val);
		}
		else if (c == 'p') pop(h);
		else if (c == 't') top(h);
		else if (c == 'd') clear(h), h = build(s);
	}
	clear(h);
	return 0;
}
```
