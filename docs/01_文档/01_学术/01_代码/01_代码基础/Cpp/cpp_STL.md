decltype(v.begin()) a;声明类型
迭代器是类中类

# 1. 序列式容器

构造方法：复制构造、花括号初始化列表（可用于 push）

### 访问元素

at()检查下标越界
rend()反向迭代器

### 插入元素

insert(iter)在迭代器指向的元素**之前**插入一个元素
push_back()
push_front()

### 删除元素

pop_back()
pop_front()
erase(iter) 返回指向下一个元素的迭代器
erase(b,e)两个迭代器之间都删除

### 容量

clear()
empty()
size()
max_size()
resize()重新设置大小

### 赋值和交换

c1 = c2 删除 c1 数据，将 c2 复制给 c1
c.assign(b,e) 删除 c 数据，将 b,e 迭代器的数据复制到 c
c1.swap(c2)

## vector

动态数组
成倍增加容量，resize()不行的时候，保持容量不变

## array

静态数组

## deque

双端队列

## list

链表

# 2. 关联式容器

## map

本质是红黑树
构造

```c++
map<K,T> m = {
    {……}，
    {……}
}
```

### 插入元素

m.insert({"h",10})
m["h"]=10';

### 查找元素

find(k) 查找键值，如果没有找到，返回 m.end()
count(k) 查找键值出现的次数

### 删除元素

erase(k) 删除键值
erase(iter)
erase(b,e)

multimap：支持重复元素的 map
lower_bound(k) 返回迭代器，指向容器第一个键值>=k 的元素
upper_bound(k) 返回迭代器，指向容器第一个键值>k 的元素
equal_range(k) 返回一个 pair 包含两个迭代器，就是上面两个

unordered_map：无序的 map

## set

multiset、unordered_set

# 3. 容器适配器

## 1. stack

功能接口
push(item)
pop()
top()
empty()

可以建立在 vector、list、deque，默认 deque

## 2. queue

push(item)
pop()
front()
back()
empty()
size()

只能建立在 list、deque，默认 deque

## 3. priority_queue

默认从大到小
size()
push(item)
pop()
top() 返回最大值
empty()

只能建立在 vector、deque，默认 vector

# 算法
