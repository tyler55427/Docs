# 八、STL 容器与算法

## 通用操作

所有容器（序列式、关联式、适配器）都支持：

| 操作 | 说明 |
|------|------|
| `empty()` | 是否为空 |
| `size()` | 元素个数 |
| `max_size()` | 可容纳的最大元素数 |
| `clear()` | 清空所有元素 |
| `swap(c2)` | 交换两个容器的数据 |

> 构造方法：复制构造、`{}` 初始化列表（可用于 `push`）。

---

## 序列式容器

### vector

动态数组，容量**成倍**增长：

```cpp
vector<int> v = {1, 2, 3};
v.push_back(4);    // 动态增长
v.resize(10);       // 调整大小
```

| vector 独有操作 | 说明 |
|----------------|------|
| `at()` / `[]` | 下标访问，越界时 `at()` 抛异常 |
| `data()` | 返回底层数组指针 |
| `capacity()` | 当前容量 |
| `reserve(n)` | 预分配至少 n 个元素空间 |
| `shrink_to_fit()` | 释放多余容量 |

### deque

双端队列，支持两端高效插入删除：

```cpp
deque<int> d;
d.push_back(1);
d.push_front(0);
```

| deque 独有操作 | 说明 |
|---------------|------|
| `at()` / `[]` | 下标访问 |
| `push_front()` / `pop_front()` | 头部插入/删除 |
| `push_back()` / `pop_back()` | 尾部插入/删除 |

### list

双向链表，支持任意位置高效插入删除，不支持下标随机访问：

```cpp
list<int> lst = {1, 2, 3};
lst.push_front(0);
lst.sort();
```

| list 独有操作 | 说明 |
|--------------|------|
| `push_front()` / `pop_front()` | 头部插入/删除 |
| `push_back()` / `pop_back()` | 尾部插入/删除 |
| `insert(iter, val)` | 在迭代器位置插入 |
| `erase(iter)` | 删除迭代器指向元素 |
| `remove(val)` | 删除所有匹配值的元素 |
| `sort()` | 链表自身排序（O(n log n)） |
| `unique()` | 删除连续重复元素 |
| `merge(list&)` | 合并两个已排序链表 |
| `splice(iter, list)` | 将另一个链表的部分移动到本链表 |

### array

固定大小的静态数组（`array<int, 5>`），大小在编译时确定：

```cpp
array<int, 4> arr = {1, 2, 3, 4};
arr.fill(0);  // 全部填充为 0
```

| array 独有操作 | 说明 |
|---------------|------|
| `at()` / `[]` | 下标访问 |
| `fill(val)` | 填充所有元素 |
| `tuple_size<T>::value` | 编译时获取大小 |

---

## 关联式容器

> 本质是**红黑树**实现，自动有序。

### map / multimap

```cpp
map<string, int> m = {
    {"Alice", 85},
    {"Bob", 92}
};
m.insert({"Carol", 78});
m["David"] = 88;        // 下标访问（不存在则插入）
```

| map / multimap 独有操作 | 说明 |
|------------------------|------|
| `operator[k]` | 按键访问，不存在则插入 |
| `find(k)` | 查找键值，返回迭代器；未找到返回 `end()` |
| `count(k)` | 键值出现次数（`multimap` > 1） |
| `erase(k)` | 按键删除 |
| `lower_bound(k)` | 第一个键值 `>= k` 的迭代器 |
| `upper_bound(k)` | 第一个键值 `> k` 的迭代器 |
| `equal_range(k)` | 返回 `pair<lower, upper>` |
| `insert(pair)` | 插入键值对 |
| `at(k)` | 按键访问，不存在则抛异常 |

```cpp
auto range = m.equal_range("Bob");
for (auto it = range.first; it != range.second; ++it)
    cout << it->first << ": " << it->second << endl;
```

`unordered_map`：基于哈希表实现，无序但查找接近 O(1)。

### set / multiset

只包含关键字，没有值。`multiset` 支持重复关键字。

| set / multiset 独有操作 | 说明 |
|-------------------------|------|
| `find(k)` | 查找关键字，返回迭代器 |
| `count(k)` | 关键字出现次数 |
| `erase(k)` | 按关键字删除 |
| `lower_bound(k)` | 第一个关键字 `>= k` 的迭代器 |
| `upper_bound(k)` | 第一个关键字 `> k` 的迭代器 |
| `equal_range(k)` | 返回 `pair<lower, upper>` |
| `insert(k)` | 插入关键字 |

---

## 容器适配器

适配器是对容器的封装，不支持迭代器、插入、删除操作。

### stack

```cpp
stack<int> s;
s.push(item); s.pop(); s.top(); s.empty();
```

| stack 操作 | 说明 |
|-----------|------|
| `push(item)` | 入栈 |
| `pop()` | 弹出栈顶（无返回值） |
| `top()` | 访问栈顶元素 |
| `empty()` | 是否为空 |
| `size()` | 元素个数 |

默认基于 `deque` 实现，也可指定 `vector` 或 `list`。

### queue

```cpp
queue<int> q;
q.push(item); q.pop(); q.front(); q.back(); q.empty();
```

| queue 操作 | 说明 |
|-----------|------|
| `push(item)` | 入队（尾插） |
| `pop()` | 出队（头删，无返回值） |
| `front()` | 访问队首元素 |
| `back()` | 访问队尾元素 |
| `empty()` | 是否为空 |
| `size()` | 元素个数 |

只能基于 `list` 或 `deque`，默认 `deque`。

### priority_queue

默认**最大堆**（从大到小排序）：

```cpp
priority_queue<int> pq;
pq.push(3); pq.push(1); pq.push(4);
pq.top();  // 4（最大值）
```

| priority_queue 操作 | 说明 |
|--------------------|------|
| `push(item)` | 插入元素 |
| `pop()` | 弹出堆顶（无返回值） |
| `top()` | 访问堆顶元素（最大值） |
| `empty()` | 是否为空 |
| `size()` | 元素个数 |

只能基于 `vector` 或 `deque`，默认 `vector`。

---

## 算法

### 自定义类型排序（结构体）

- **比较函数的语义差异**：
    - sort 的 `comp(a, b)` 返回 true 表示 a 排在 b 前面（升序即 `a < b`）；
    - priority_queue 的 `comp(a, b)` 返回 true 表示 a 的优先级低于 b（所以默认 `less` 下 top 为最大值，换成 `greater` 则 top 为最小值）。

#### 方式一：重载 `<` 运算符

```cpp
struct Student {
    string name;
    int score;
    bool operator<(const Student& other) const {
        return score > other.score;  // 降序
    }
};
sort(v.begin(), v.end());
```

#### 方式二：传入比较函数

```cpp
struct Student { string name; int score; };

bool compareByScoreDesc(const Student& a, const Student& b) {
    return a.score > b.score;
}
sort(v.begin(), v.end(), compareByScoreDesc);
```

#### 方式三：lambda 表达式（C++11）

```cpp
sort(v.begin(), v.end(),
    [](const Student& a, const Student& b) {
        return a.score > b.score;
    });
```

> lambda 语法：`[捕获列表](参数) -> 返回类型 { 函数体 }`
