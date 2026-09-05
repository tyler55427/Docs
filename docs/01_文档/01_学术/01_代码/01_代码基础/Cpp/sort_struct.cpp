// 结构体排序的三种实现方式
// 题目描述：给定一组学生信息（姓名、成绩），按成绩从高到低排序
// 演示三种实现方式：
//   1. 运算符重载 <（结构体内置比较）
//   2. sort() 传入自定义比较函数（函数指针）
//   3. lambda 表达式（C++11 特性）
// 应用场景：自定义类型排序、多关键字排序

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

// ===================== 方式 1：运算符重载 < =====================

struct Student1 {
    string name;
    int score;

    // 重载 < 运算符：按 score 从高到低排序（返回值含义：this 严格小于 other）
    // 注意：与 sort 默认的"严格弱序"配合，反向排序用 this.score > other.score
    bool operator<(const Student1& other) const {
        return score > other.score;  // 降序
    }
};

void sortByOperator() {
    cout << "=== 方式 1：运算符重载 < ===" << endl;
    vector<Student1> v = {
        {"Alice", 85},
        {"Bob", 92},
        {"Carol", 78}
    };
    sort(v.begin(), v.end());
    for(const auto& s : v)
        cout << s.name << " " << s.score << endl;
}

// ===================== 方式 2：sort 传入比较函数 =====================

struct Student2 {
    string name;
    int score;
};

// 自定义比较函数（全局函数或静态函数）
// 返回 true 表示 a 应排在 b 前面
bool compareByScoreDesc(const Student2& a, const Student2& b) {
    return a.score > b.score;
}

void sortByFunction() {
    cout << "=== 方式 2：sort 传入比较函数 ===" << endl;
    vector<Student2> v = {
        {"Alice", 85},
        {"Bob", 92},
        {"Carol", 78}
    };
    // 将比较函数作为第三个参数传入 sort
    sort(v.begin(), v.end(), compareByScoreDesc);
    for(const auto& s : v)
        cout << s.name << " " << s.score << endl;
}

// ===================== 方式 3：lambda 表达式 =====================

struct Student3 {
    string name;
    int score;
};

void sortByLambda() {
    cout << "=== 方式 3：lambda 表达式 ===" << endl;
    vector<Student3> v = {
        {"Alice", 85},
        {"Bob", 92},
        {"Carol", 78}
    };
    // lambda 表达式：[capture](args) { body }
    // 这里捕获列表为空，参数为两个 const Student3&
    sort(v.begin(), v.end(),
         [](const Student3& a, const Student3& b) {
             return a.score > b.score;
         });
    for(const auto& s : v)
        cout << s.name << " " << s.score << endl;
}

int main() {
    sortByOperator();
    cout << endl;
    sortByFunction();
    cout << endl;
    sortByLambda();
    return 0;
}
