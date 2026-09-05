#include <iostream>
using namespace std;


class Complex
{
private:
    double real, image; // 复数的实部与虚部
public:
    Complex(double r = 0, double i = 0); // 构造函数
    Complex(const Complex &other);       // 拷贝构造函数
    void print();                        // 打印复数

    Complex operator+(const Complex &other); // 重载加法运算符（二元）
    Complex operator-(const Complex &other); // 重载减法运算符（二元）
    Complex operator-();                     // 重载求负运算符（一元）
    Complex operator=(const Complex &other); // 重载赋值运算符（二元）

    Complex &operator++();   // 重载前置++
    Complex operator++(int); // 重载后置++
    Complex &operator--();   // 重载前置--
    Complex operator--(int); // 重载后置--
};

Complex::Complex(double r, double i) {
        real = r;
        image = i;
} // 构造函数

Complex::Complex(const Complex& other) {
        real = other.real;
        image = other.image;
}       // 拷贝构造函数

void Complex::print() {
    cout << real;
    if(image>0) cout << "+" << image << "i" << endl;
    else cout << image << "i" << endl;
}  // 打印复数
Complex Complex::operator+(const Complex &other){
    return Complex(real + other.real,image + other.image);
} // 重载加法运算符（二元）

Complex Complex::operator-(const Complex& other) {
    return Complex(real - other.real,image - other.image);
} // 重载减法运算符（二元）

Complex Complex::operator-() {
    return Complex(-real,-image);
}  // 重载求负运算符（一元）

Complex Complex::operator=(const Complex& other) {
    this->real = other.real;
    this->image = other.image;
    return *this;
} // 重载赋值运算符（二元）
Complex& Complex::operator++(){
    real++;image++;
    return *this;
}   // 重载前置++

Complex Complex::operator++(int) {
    Complex temp(real++,image++);
    return temp;
} // 重载后置++

Complex& Complex::operator--() {
    real--;image--;
    return *this;
}   // 重载前置--

Complex Complex::operator--(int) {
    Complex temp(real--,image--);
    return temp;
} // 重载后置--