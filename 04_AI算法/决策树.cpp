#include <iostream>
using namespace std;
#include <vector>
#include <cmath>

double threshold[30];
int train[1010][30];
int label[1010];
int test[1010][30];
int ans_label[1010];

typedef struct tree {
    int index;
    int cls;
    int l, r;
} tree;

tree ans[10010];
int cnt = 0;
bool sign[30];
int n, m;

// 计算信息熵
double h(int all, int cnt1) {
    if (all == 0) return 0.0;
    int cnt0 = all - cnt1;
    double p1 = 1.0 * cnt1 / all;
    double p2 = 1.0 * cnt0 / all;
    // 如果p1或p2为0，返回0代表信息增益最大
    if (abs(p1) < 1e-8 or abs(p2) < 1e-8) return 0.0;
    return -p1 * log(p1) - p2 * log(p2);
}

// 计算某个特征的信息增益
double get_value(vector<int>& v, int index) {
    // index特征为1的样本数
    int cnt1 = 0;
    // index特征为1且类别为1的样本数，index特征为0且类别为1的样本数
    int cnty11 = 0, cnty01 = 0;
    for (auto& i : v) {
        cnt1 += train[i][index];
        if (train[i][index]) cnty11 += label[i];
        else cnty01 += label[i];
    }
    int len = v.size();
    // 信息增益 = 原信息熵 - 条件信息熵，因为原信息熵是固定的，所以我们只需要计算条件信息熵即可
    double original_entropy = h(len, cnty01 + cnty11);
    double cond_entropy = 0.0;
    cond_entropy += 1.0 * cnt1 / len * h(cnt1, cnty11);
    cond_entropy += 1.0 * (len - cnt1) / len * h(len - cnt1, cnty01);
    return original_entropy - cond_entropy;
}

void build_tree(vector<int>& v, int now) {
    // 1. 如果当前节点的样本全为同一个类别，保证左右子树不为空
    int sum = 0;
    for (auto& i : v) {
        sum += label[i];
    }
    if (sum == 0 || sum == v.size()) {
        ans[now].cls = sum ? 1 : 0;
        return;
    }

    double mv = 0.0;
    int index = -1;
    for (int i = 0; i < m; ++i) {
        if (!sign[i]) {
            double tmp = get_value(v, i);
            if (tmp > mv) {
                mv = tmp;
                index = i;
            }
        }
    }
    // 2. 如果所有特征都被使用过了
    // 3. 如果某个特征的取值一样，信息增益<0
    if (index == -1) {
        int cnt1 = 0;
        for (auto& i : v) {
            cnt1 += label[i];
        }
        ans[now].cls = (cnt1 * 2 > v.size()) ? 1 : 0;
        return;
    }

    vector<int> left, right;
    for (auto& i : v) {
        if (train[i][index] == 0) {
            left.push_back(i);
        }
        else {
            right.push_back(i);
        }
    }
    int ll = ++cnt;
    int rr = ++cnt;
    ans[now].index = index;
    ans[now].l = ll;
    ans[now].r = rr;
    sign[index] = true;
    build_tree(left, ll);
    build_tree(right, rr);
    // 返回父节点的时候要把当前特征标记为未使用过
    sign[index] = false;
}

int query(int now, int i) {
    while(ans[now].l) {
        if (test[i][ans[now].index] == 0) {
            now = ans[now].l;
        }
        else {
            now = ans[now].r;
        }
    }
    return ans[now].cls;
}

int main() {
    // 训练数据个数，特征个数
    cin >> n >> m;
    double x;
    vector<int> v;
    // 每个特征的阈值
    for (int i = 0; i < m; ++i) cin >> threshold[i];
    // 训练数据
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> x;
            if (x < threshold[j]) train[i][j] = 0;
            else train[i][j] = 1;
        }
        cin >> label[i];
        v.push_back(i);
    }
    build_tree(v, 0);

    // 测试数据
    int q;
    cin >> q;
    for (int i = 0; i < q; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> x;
            if (x < threshold[j]) test[i][j] = 0;
            else test[i][j] = 1;
        }
        ans_label[i] = query(0, i);
    }
    for (int i = 0; i < q; ++i) {
        cout << ans_label[i] << " ";
    }
}
/*
30 5
58.8 25.0 83.8 42.6 59.3
6.9 24.6 44.3 19.1 56.1 0
20.1 68.2 21.1 31.8 36.6 0
2.8 30.3 13.2 68.5 41.0 1
67.2 59.6 19.7 10.4 10.6 1
18.6 80.1 64.0 68.0 91.2 0
67.5 45.7 60.4 62.2 48.1 0
20.3 98.6 46.2 42.7 97.1 0
45.7 57.3 51.4 81.6 83.1 1
19.3 14.6 33.6 55.7 45.5 0
26.2 89.8 89.8 83.1 78.1 1
69.8 5.4 12.2 51.0 60.2 1
47.1 8.8 0.6 70.9 46.4 0
39.6 70.3 59.5 85.3 94.8 1
66.6 59.4 80.7 50.4 3.8 1
37.5 65.9 85.3 63.6 33.1 0
29.7 23.0 91.6 76.9 39.1 1
89.0 14.2 75.3 43.2 61.6 1
97.8 38.8 86.2 15.9 33.2 1
8.9 41.6 79.4 81.3 17.9 1
76.7 24.7 11.4 7.3 78.6 1
95.6 6.9 24.9 17.6 77.5 1
7.7 26.7 97.0 86.2 80.5 1
28.5 49.3 34.6 89.5 67.6 1
85.6 59.4 79.3 30.0 23.1 1
21.9 66.7 35.0 82.9 88.8 1
9.0 31.1 43.5 13.4 5.0 0
39.0 61.5 23.0 4.2 38.6 0
12.2 72.5 79.1 50.4 84.9 1
96.9 98.0 70.8 63.7 51.8 1
65.6 32.1 9.6 75.2 73.2 1
20
86.6 83.5 17.0 70.7 34.1
7.0 68.9 63.9 60.4 68.2
43.5 92.4 48.5 54.6 94.4
67.6 16.1 34.5 96.7 82.1
41.1 26.2 99.7 10.1 17.2
55.7 9.7 86.0 92.5 22.1
76.9 75.8 52.6 75.5 18.2
49.4 76.0 47.5 7.5 55.1
46.1 36.4 5.6 74.4 84.3
47.7 80.0 33.5 29.7 68.7
56.3 10.3 30.5 32.9 59.6
57.8 52.6 18.6 45.5 83.6
86.7 73.5 81.4 66.6 40.7
81.0 48.6 94.1 76.9 98.1
21.9 81.1 17.8 28.7 21.5
85.2 81.9 43.7 33.1 17.7
2.5 64.9 95.2 5.1 71.4
5.3 85.7 82.8 42.2 54.6
91.5 44.2 81.6 90.7 33.2
96.3 79.9 50.9 18.5 91.0
*/