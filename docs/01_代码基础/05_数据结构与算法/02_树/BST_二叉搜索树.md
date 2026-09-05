# BST 二叉搜索树

## 结构定义

二叉搜索树节点结构，包含值和左右孩子指针。

```cpp
int arr[1000009];
int p[110]={1,2,4,8,16,32,64,128,256,512,1024,2048,4096};

struct BN
{
	int v;
	BN* l,*r;
	BN(int x,BN* l=nullptr,BN* r=nullptr):v(x),l(l),r(r)
	{};
};

typedef BN* T;
```

## 基本操作

计算树的深度、判断是否包含某值。

### 计算深度

```cpp
int depth(T t)
{
	if(t==nullptr) return -1;
	return max(depth(t->l),depth(t->r))+1;
}
```

### 查找

```cpp
bool contain(T t,int x)
{
	if(t==nullptr) return false;
	else if(t->v<x) return contain(t->l,x);
	else if(t->v>x) return contain(t->r,x);
	else return true;
}
```

### 查找最小节点

返回指针，可以保证边界：结点为空时返回 nullptr。

```cpp
T fmin(T t)
{
	if(t==nullptr) return nullptr;
	else if(t&&!t->l) return t;
	else if(t->l) return fmin(t->l);
}
```

### 查找最大节点

```cpp
T fmax(T t)
{
	if(t)
		while(t->r)
			t=t->r;
	return t;
}
```

## 插入与删除

插入新节点，删除时分三种情况处理。

### 插入

也可以用返回指针的方法。

```cpp
void insert(T &t,int x)
{
	if(t==nullptr)
	{
		t=new BN{x};
	}
	else if(x<t->v) insert(t->l,x);
	else if(x>t->v) insert(t->r,x);
}
```

### 删除

删除要分三种情况。

```cpp
void remove(T &t,int x)
{
	if(t==nullptr) return;
	else if(x<t->v) remove(t->l,x);
	else if(x>t->v) remove(t->r,x);
	else if(t->l&&t->r)
	{
		t->v=fmin(t->r)->v;
		remove(t->r,t->v);
	}
	else
	{
		T old=t;
		t=(t->l)?t->l:t->r;
		delete old;
	}
}
```

## 遍历与打印

### 层序存储

```cpp
void tra(T &t,int i)
{
	if(t)
	{
		arr[i]=t->v;
		tra(t->l,2*i);
		tra(t->r,2*i+1);
	}
}
```

### 判断层序位置

```cpp
int ceng(int x)
{
	for(int i=0;i<=12;++i)
	{
		if(x==p[i]) return i;
	}
	return -1;
}
```

### 打印树结构

```cpp
void bl(T &t)
{
	int n=depth(t);
	if(n==-1) cout<<"nullptr";
	for(int i=1;i<p[n+1];++i)
	{
		if(ceng(i)!=-1)
		{
			cout<<endl;
			for(int j=n-ceng(i);j>0;--j) cout<<" ";
		}
		cout<<arr[i]<<" ";
	}
	cout<<endl;
}
```

## 销毁树

```cpp
void clear(T &t)
{
	if(t)
	{
		clear(t->l);
		clear(t->r);
		delete t;
	}
}
```

## 主函数

交互式菜单，支持插入（i）、删除（r）、遍历（t）、删除整棵树（d）。

```cpp
int main()
{
	cout<<"End with '#'"<<endl;
	char c;
	T t=nullptr;
	while(true)
	{
		cout<<"Insert 'i' and a number"<<endl;
		cout<<"Remove 'r' and a number"<<endl;
		cout<<"Travel 't'"<<endl;
		cout<<"Delete 'd'"<<endl;
		cin>>c;
		if(c=='#') break;
		else if(c=='i')
		{
			int temp;
			cin>>temp;
			insert(t,temp);
		}
		else if(c=='r')
		{
			int temp;
			cin>>temp;
			remove(t,temp);
		}
		else if(c=='t')
		{
			for(int i=0;i<1000;i++) arr[i]=0;
			tra(t,1);
			bl(t);
		}
		else if(c=='d')
		{
			clear(t);
			t=nullptr;
		}
	}
	clear(t);
}
```
