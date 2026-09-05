#include <iostream>
using namespace std;

// 虚继承
class Shape {
protected:
    int id;

public:
    Shape(int id = 0) : id(id) {}

    // 虚析构：
    // 通过基类指针删除派生类对象时，必须先调用派生类的析构
    // 有虚函数的基类的析构函数必须是虚函数
    virtual ~Shape() {}

    // 虚函数：
    // 在基类中用 virtual 声明后，派生类可重写（override）。
    // 通过基类指针/引用调用时，会根据对象的真实类型动态分派到对应的重写版本，实现多态。
    virtual void draw() const {}

    // 纯虚函数：
    // 只有声明，没有实现，使类成为抽象类，不能被实例化。
    // 派生类必须重写，否则自身也成为抽象类。
    virtual void area() const = 0;
};

/* 虚继承：保证 Circle 中只有一份 Shape */
class Color : virtual public Shape {
    string color;

public:
    // 虚继承中，最派生类（Circle）负责构造共同基类（Shape），
    // 因此 Color 的构造函数不直接初始化 Shape。
    Color(const string& c = "black") : color(c), Shape() {}

    virtual ~Color() {}

    void setColor(const string& c) { color = c; }

    // 虚函数重写
    void draw() const override {}
};

class TwoD : virtual public Shape {
    int x, y;

public:
    TwoD(int x = 0, int y = 0) : x(x), y(y), Shape() {}

    virtual ~TwoD() {}

    void draw() const override {}
};

class Circle : public Color, public TwoD {
    double radius;

public:
    // 虚继承中，由最派生类直接调用 Shape 的构造函数
    Circle(int id, const string& c, int x, int y, double r) : Color(c), TwoD(x, y), Shape(id), radius(r) {}

    ~Circle() override {}

    // 重写：最终调用 Circle 的版本
    void draw() const override {}

    // 实现纯虚函数
    void area() const override {}
};

/*================ main ================*/
int main()
{
    // 多态：通过基类指针调用，动态分派到 Circle 的 draw()
    Shape* p = new Circle(1, "red", 0, 0, 5);
    p->draw();   // draw Circle r=5
    p->area();   // area = 78.5

    delete p;

    return 0;
}
