# AC自动机（多模式串匹配）

## AC 自动机（Aho-Corasick Auto Machine）

**题目描述**：多模式串匹配——在文本串 s 中同时查找 n 个模式串的出现次数

**解法**：AC 自动机（KMP 在多模式串场景的扩展）

**核心思想**：在 Trie 树上构建 fail 指针，实现 O(|s| + 所有模式串总长 + 匹配次数) 的高效匹配

**应用场景**：敏感词过滤、病毒特征检测、字符串统计等

## Trie 树节点

```cpp
struct Node {
    int next[26];  // 26 个子节点指针（下标表示字符）
    int out;       // 匹配计数（以该节点为结尾的模式串出现次数）
    int fail;      // fail 指针（失配时跳转的节点）
    int indeg;     // 入度（用于拓扑排序统计）
    int id;        // 节点编号
};
```

## 初始化

```cpp
void init() {
    nodeCnt = 0;
    memset(result, 0, sizeof(result));
    node[0].init();
    node[0].id = 0;
}
```

## 插入模式串，构建 Trie 树

```cpp
void insert(const char* pat, int patIdx) {
    int u = 0;  // 从根节点开始
    for(int i = 0; pat[i]; ++i) {
        int c = pat[i] - 'a';
        if(!node[u].next[c]) {
            node[u].next[c] = ++nodeCnt;
            node[nodeCnt].init();
            node[nodeCnt].id = nodeCnt;
        }
        u = node[u].next[c];
    }
    node[u].out++;
    patId[patIdx] = u;
}
```

## 构建 fail 指针（BFS 遍历）

**说明**：fail[u] = 从根到 u 的字符串的最长真后缀，同时也是某个前缀的节点编号，相当于 KMP 中 next 数组在多模式串上的扩展

```cpp
void buildFail() {
    queue<int> q;

    // 1. 先将与根节点直接相连的节点入队，它们的 fail 指向根（0）
    for(int c = 0; c < 26; ++c) {
        int child = node[0].next[c];
        if(child) {
            q.push(child);
        }
    }

    // 2. BFS 遍历，层层构建 fail 指针
    while(!q.empty()) {
        int u = q.front();
        q.pop();

        for(int c = 0; c < 26; ++c) {
            int child = node[u].next[c];
            if(child) {
                node[child].fail = node[node[u].fail].next[c];
                q.push(child);
            } else {
                node[u].next[c] = node[node[u].fail].next[c];
            }
        }
        if(node[u].fail != u)
            node[node[u].fail].indeg++;
    }
}
```

## 在文本串上匹配

```cpp
void query(const char* text) {
    int u = 0;  // 从根节点开始
    for(int i = 0; text[i]; ++i) {
        int c = text[i] - 'a';
        u = node[u].next[c];
        node[u].out++;
    }
}
```

## 拓扑排序统计完整匹配次数

**说明**：将子节点的计数累加到 fail 父节点。由于 node[u].out 只记录了以 u 为结尾的直接匹配，需要沿 fail 链向上传播，才能得到完整的匹配次数

```cpp
void topoSortCount() {
    queue<int> q;

    for(int i = 0; i <= nodeCnt; ++i) {
        if(node[i].indeg == 0)
            q.push(i);
    }

    while(!q.empty()) {
        int u = q.front();
        q.pop();

        result[node[u].id] = node[u].out;
        int f = node[u].fail;
        node[f].out += node[u].out;

        if(!--node[f].indeg)
            q.push(f);
    }
}
```
