#include <iostream>
using namespace std;
#include <algorithm>
#include <cmath>

typedef struct pack {
    int id;
    double x, y;
} pack;

pack arr[110];
pack ks[11];
int distribute[110];
pack zero;

double get_dis(pack a, pack b) {
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

bool cmp(pack a, pack b) {
    double dis_a = get_dis(a, zero), dis_b = get_dis(b, zero);
    if (abs(dis_a - dis_b) < 1e-10) return a.id < b.id;
    return dis_a < dis_b;
}

int main() {
    zero.x = 0.0;
    zero.y = 0.0;
    zero.id = -1;
    int k, n;
    cin >> k >> n;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i].x >> arr[i].y;
        arr[i].id = i;
    }
    double dis = 0.0;
    if (k >= n) {
        sort(arr, arr + n, cmp);
        for (int i = 0;i < n;++i) {
            cout << arr[i].x << " " << arr[i].y << endl;
        }
    }
    else {

        sort(arr, arr + n, cmp);

        for (int i = 0;i < k;++i) {
            ks[i].x = arr[i].x;
            ks[i].y = arr[i].y;
        }

        int cnt = 0;
        double tmp;
        while (cnt < 50) {
            cnt++;
            // 将每个点分配到最近的中心点
            for (int i = 0;i < n;++i) {
                double minv = 1e9;
                for (int j = 0;j < k;++j) {
                    tmp = get_dis(arr[i], ks[j]);
                    if (tmp < minv) {
                        minv = tmp;
                        distribute[i] = j;
                    }
                }
            }

            // 更新中心点位置
            double update_sum = 0.0;
            int cnt_k;
            for (int i = 0;i < k;++i) {
                cnt_k = 0;
                pack temp;
                temp.x = 0.0;
                temp.y = 0.0;
                for (int j = 0;j < n;++j) {
                    if (distribute[j] == i) {
                        cnt_k++;
                        temp.x += arr[j].x;
                        temp.y += arr[j].y;
                    }
                }
                if (cnt_k) {
                    temp.x /= cnt_k;
                    temp.y /= cnt_k;
                    update_sum += get_dis(temp, ks[i]);
                    ks[i] = temp;
                }
            }
            if (update_sum < 1e-4) break;
        }

        sort(ks, ks + k, cmp);
        for (int i = 0;i < k;++i) {
            cout << ks[i].x << " " << ks[i].y << endl;
        }
    }
}