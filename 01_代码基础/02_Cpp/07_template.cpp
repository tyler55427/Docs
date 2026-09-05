#include <iostream>
#include <typeinfo>
#include <algorithm> // swap
#include <cstring>   // strcmp

using namespace std;

// ==================== 1. 函数模板 ====================
template <typename T>
T maxOf(T a, T b) {
    return (a > b) ? a : b;
}

// ==================== 2. 类模板 ====================
template <typename T1, typename T2>
class Pair {
public:
    T1 first;
    T2 second;

    Pair(T1 f, T2 s) : first(f), second(s) {}

    void print() const {
        cout << "  Pair<" << typeid(T1).name() << ", "
             << typeid(T2).name() << ">: ("
             << first << ", " << second << ")\n";
    }
};

// ==================== 3. 全特化 ====================
template <>
class Pair<const char*, const char*> {
    const char* first;
    const char* second;

public:
    Pair(const char* f, const char* s) : first(f), second(s) {}

    // 用 strcmp 比较字符串
    bool operator==(const Pair& rhs) const {
        return strcmp(first, rhs.first) == 0
            && strcmp(second, rhs.second) == 0;
    }

    void print() const {
        cout << "  Pair<const char*, const char*>: \""
             << first << "\", \"" << second << "\"\n";
    }
};

// ==================== 4. 偏特化 ====================
template <typename T>
class Pair<T, T> {
    T first, second;

public:
    Pair(T f, T s) : first(f), second(s) {}

    // 用 swap 交换两个相同类型的元素
    void swap() {
        std::swap(first, second);
    }

    void print() const {
        cout << "  PairSame<" << typeid(T).name() << ">: ("
             << first << ", " << second << ")\n";
    }
};

int main() {
    // ---- 1. 函数模板 ----
    cout << "========== 1. 函数模板 ==========\n";
    cout << "  max(3, 7)     = " << maxOf(3, 7) << "\n";
    cout << "  max(2.5, 3.7) = " << maxOf(2.5, 3.7) << "\n";

    // ---- 2. 类模板 ----
    cout << "\n========== 2. 类模板 ==========\n";
    Pair<int, double> p1(42, 3.14);
    p1.print();

    // ---- 3. 全特化 ----
    cout << "\n========== 3. 全特化 ==========\n";
    Pair<const char*, const char*> p2("Hello", "World");
    p2.print();
    Pair<const char*, const char*> p3("Hello", "World");
    cout << "  p2 == p3: " << (p2 == p3) << "\n";

    // ---- 4. 偏特化 ----
    cout << "\n========== 4. 偏特化 ==========\n";
    Pair<int, int> p4(10, 20);
    p4.print();
    p4.swap();
    p4.print();

    return 0;
}
