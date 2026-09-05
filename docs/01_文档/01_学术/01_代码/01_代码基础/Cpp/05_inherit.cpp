#include<iostream>
using namespace std;

class Base {
public:
    Base(int a) {
        this->a = a;
        cout << "Base构造" << endl;
    }
    ~Base() {
        cout << "Base析构" << endl;
    }
    int a = 0;
};

class S1 {
    Base base;
public:
    // 基类只能在初始化列表中初始化，不能在构造函数体中初始化
    S1() : base(0) {
        cout << "S1构造" << endl;
    }
    ~S1() {
        cout << "S1析构" << endl;
    }
};

class S2 : public Base {
public:
    S2(int a) : Base(a) {
        cout << "S2构造" << endl;
    }
    ~S2() {
        cout << "S2析构" << endl;
    }
    int a = 1;
};

void test1() {
    S1 s1;
}

void test2() {
    S2 s2(5);
    // 同名变量，添加作用域访问
    cout << s2.a << endl;
    cout << s2.Base::a << endl;
}

int main() {
    // 创建对象正常虚构，但是使用基类指针创建对象，需要虚析构
    test1();
    test2();
    return 0;
}