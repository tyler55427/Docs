# AVL_平衡二叉树

## 结构体定义

AVL 树节点，包含值、左右孩子指针和高度。

```cpp
struct AvlNode
{
	int v;
	AvlNode* l;
	AvlNode* r;
	int h;
	AvlNode(int v,AvlNode* l=nullptr,AvlNode* r=nullptr,int h=0):v(v),l(l),r(r),h(h)
	{}
};
```

全局数组用于层序遍历打印。

```cpp
int arr[1000009];
int p[110]={1,2,4,8,16,32,64,128,256,512,1024,2048,4096};
int allow=1;
```

获取节点高度，空节点返回 -1。

```cpp
int height(AvlNode* t)
{
	return t==nullptr?-1:t->h;
}
```

## 旋转操作

AVL 树通过旋转保持平衡，包含单旋（左右旋）和双旋（左右旋组合）。

### 左旋 (rl)

k1 是左子树，k2 是根。先把 k2 的左孩子换成 k1 的右孩子，再把 k1 的右孩子换成 k2，防止没有指针指向 k2 的内存。

```cpp
void rl(AvlNode* &k2)
{
	AvlNode* k1=k2->l;
	k2->l=k1->r;
	k1->r=k2;
	k2->h=max(height(k2->l),height(k2->r))+1;
	k1->h=max(height(k1->l),k2->h)+1;
	k2=k1;
}
```

### 右旋 (rr)

```cpp
void rr(AvlNode* &k1)
{
	AvlNode* k2=k1->r;
	k1->r=k2->l;
	k2->l=k1;
	k1->h=max(height(k1->l),height(k1->r))+1;
	k2->h=max(height(k2->r),k1->h)+1;
	k1=k2;
}
```

### 左右旋 (drl)

先对左子树右旋，再对根左旋。

```cpp
void drl(AvlNode* &k3)
{
	rr(k3->l);
	rl(k3);
}
```

### 右左旋 (drr)

先对右子树左旋，再对根右旋。

```cpp
void drr(AvlNode* &k3)
{
	rl(k3->r);
	rr(k3);
}
```

## 平衡调整

根据左右子树高度差决定旋转方式。

```cpp
void balance(AvlNode* &t)
{
	if(t==nullptr) return;
	if(height(t->l)-height(t->r)>allow)
		if(height(t->l->l)>=height(t->l->r))
			rl(t);
		else
			drl(t);
	else if(height(t->r)-height(t->l)>allow)
		if(height(t->r->r)>=height(t->r->l))
			rr(t);
		else
			drr(t);
	t->h=max(height(t->l),height(t->r))+1;
}
```

## 插入与删除

递归插入新节点，插入后进行平衡调整。删除时若左右子树均存在，用后继节点替换。

### 插入

```cpp
void insert(AvlNode* &t,int x)
{
	if(t==nullptr)
		t=new AvlNode{x};
	else if(x<t->v)
		insert(t->l,x);
	else if(x>t->v)
		insert(t->r,x);

	balance(t);
}
```

### 删除

```cpp
void remove(AvlNode* &t,int x)
{
	if(t==nullptr) return;
	if(x<t->v) remove(t->l,x);
	else if(x>t->v) remove(t->r,x);
	else if(t->l&&t->r)
	{
		t->v=fmin(t->r)->v;
		remove(t->r,t->v);
	}
	else
	{
		AvlNode* old=t;
		t=(t->l)?t->l:t->r;
		delete old;
	}
	balance(t);
}
```

### 查找最小节点

递归查找最小节点，递归为空时返回 nullptr。

```cpp
AvlNode* fmin(AvlNode* t)
{
	if(t==nullptr) return nullptr;
	else if(t&&!t->l) return t;
	else if(t->l) return fmin(t->l);
}
```

### 查找最大节点

```cpp
AvlNode* fmax(AvlNode* t)
{
	if(t)
		while(t->r)
			t=t->r;
	return t;
}
```

## 遍历与打印

### 层序遍历存储

将树按层序存储到数组中。

```cpp
void tra(AvlNode* &t,int i)
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
void bl(AvlNode* &t)
{
	int n=height(t);
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
void clear(AvlNode* &t)
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

交互式 AVL 树操作菜单，支持插入（i）、删除（r）、遍历（t）、清空（d）。

```cpp
int main()
{
	cout<<"End with '#'"<<endl;
	char c;
	AvlNode* t=nullptr;
	while(true)
	{
		cout<<"Insert 'i' and a number"<<endl;
		cout<<"Remove 'r' and a number"<<endl;
		cout<<"Travel 't'"<<endl;
		cout<<"Clear 'd'"<<endl;
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
