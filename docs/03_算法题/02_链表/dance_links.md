## Dance Links（舞蹈链）

**问题描述**：给定一个 n 行 m 列的矩阵，矩阵中包含 0 和 1 元素。使用舞蹈链（Dancing Links）算法求解精确覆盖问题，输出任意一组可行解。

**解法**：舞蹈链算法是一种用于解决精确覆盖问题的数据结构，利用双向循环链表实现高效的选择和回溯。通过哨兵节点简化边界处理，使用启发式选择（选择 1 的数量最少的列）加速搜索。

```cpp
constexpr int N = 500 + 10;
int n, m, ans;
int stk[N];

struct DLX {
    static constexpr int MAXSIZE = 1e5 + 10;
    int n, m, tot, first[MAXSIZE + 10], siz[MAXSIZE + 10];
    int L[MAXSIZE + 10], R[MAXSIZE + 10], U[MAXSIZE + 10], D[MAXSIZE + 10];
    // 保存节点的数组
    int col[MAXSIZE + 10], row[MAXSIZE + 10];

    void build(const int& r, const int& c) {  // 进行build操作
        n = r, m = c;
        for (int i = 0; i <= c; ++i) {
            // 哨兵和数据共用一个L, R数组，用于直接锁定列
            L[i] = i - 1, R[i] = i + 1;
            // 头尾相连，形成一个循环链表
            U[i] = D[i] = i;
        }
        // 最后特殊化处理，不用再循环中额外判断
        L[0] = c, R[c] = 0, tot = c;
        memset(first, 0, sizeof(first));
        memset(siz, 0, sizeof(siz));
    }

    void insert(const int& r, const int& c) {  // 进行insert操作
        // 和前向星类似的操作
        // 由于上下左右连接的问题，还是需要有一定的顺序的
        // 能够直接使用尾指针的列表写，是因为输入数据的有序性
        col[++tot] = c, row[tot] = r, ++siz[c];
        D[tot] = D[c], U[D[c]] = tot, U[tot] = c, D[c] = tot;
        if (!first[r])
            // 用于直接锁定行，只是这个问题中没有使用到
            first[r] = L[tot] = R[tot] = tot;
        else {
            R[tot] = R[first[r]], L[R[first[r]]] = tot;
            L[tot] = first[r], R[first[r]] = tot;
        }
    }

    void remove(const int& c) {  // 进行remove操作
        int i, j;
        // 删除列，并删除列上为1的行，因为插入的时候只插入了1的元素
        L[R[c]] = L[c], R[L[c]] = R[c];
        for (i = D[c]; i != c; i = D[i])
            for (j = R[i]; j != i; j = R[j])
                U[D[j]] = U[j], D[U[j]] = D[j], --siz[col[j]];
    }

    void recover(const int& c) {  // 进行recover操作
        int i, j;
        // 向下删除，向上恢复，刚好相反的过程，但实际上不需要
        for (i = U[c]; i != c; i = U[i])
            for (j = L[i]; j != i; j = L[j])
                U[D[j]] = D[U[j]] = j, ++siz[col[j]];
        L[R[c]] = R[L[c]] = c;

        // // 洛谷上通过了
        // // 好像不需要相反的顺序恢复，虽然恢复的时候会指向不存在的节点，但是由于指向的节点一定是遍历中需要恢复的节点，因此可以直接恢复
        // L[R[c]] = R[L[c]] = c;
        // for (i = D[c]; i != c; i = D[i])
        //     for (j = L[i]; j != i; j = L[j])
        //         U[D[j]] = D[U[j]] = j, ++siz[col[j]];
    }

    bool dance(int dep) {  // dance
        if (!R[0]) {
            // 如果哨兵没有了，则列表为空
            ans = dep;
            return true;
        }
        int i, j, c = R[0];
        for (i = R[0]; i != 0; i = R[i])
            // 找到最小的列，启发式，使找到答案
            if (siz[i] < siz[c]) c = i;
        remove(c);
        for (i = D[c]; i != c; i = D[i]) {
            // 每次选择一行，上面的remove(c)已经将这一列的所有行删除了，因为这一列都有1
            stk[dep] = row[i];
            // 加速求解，将这一列有1的行全部删除，因为如果选择这些行，就会有交集
            for (j = R[i]; j != i; j = R[j]) remove(col[j]);
            // 不直接使用return dance(dep + 1)是因为需要恢复
            if (dance(dep + 1)) return true;
            for (j = L[i]; j != i; j = L[j]) recover(col[j]);
        }
        recover(c);
        return false;
    }
} solver;

using std::cin;
using std::cout;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    cin >> n >> m;
    solver.build(n, m);
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j) {
            int x;
            cin >> x;
            if (x) solver.insert(i, j);
        }

    if (solver.dance(1))
        for (int i = 1; i < ans; ++i) cout << stk[i] << ' ';
    else
        cout << "No Solution!\n";
    return 0;
}
```

**备注**：

- 舞蹈链的核心是双向循环链表，通过哨兵节点实现 O(1) 的插入和删除
- 启发式选择最少 1 的列可以显著加速搜索
- `remove` 和 `recover` 操作互为逆过程，保证回溯的正确性
