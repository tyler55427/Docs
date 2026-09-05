#include <iostream>
using namespace std;

class Person {
public:
    // 1. 无参构造
    Person() {}
    // 2. 有参构造
    // 初始化列表
    Person(int a, string n = "") : age(a), name(n) {}
    // 3. 拷贝构造
    Person(const Person& p) : age(p.age), name(p.name) {}

    // 析构函数
    ~Person() {}
private:
    int age;
    string name;
};

int main() {
    // 实例化
    // 1. 无参构造
    // 注意：不能Person p1()，这种方式实例化对象，编译器会认为是函数声明
    Person p1;
    // 2. 有参构造
    Person p2(18);
    Person p3 = Person(22);
    Person p4 = { 20 };
    Person(10); // 匿名对象，构造完后立即销毁
    // 3. 拷贝构造
    Person p5 = p4;
    Person p6(p4);

    return 0;
}
