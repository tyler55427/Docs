#include <iostream>
using namespace std;

class Vec3
{
    double x, y, z;

public:
    Vec3(double x = 0, double y = 0, double z = 0) : x(x), y(y), z(z) {}

    // 类内定义 
    Vec3 operator+(const Vec3& b) {
        return Vec3(x + b.x, y + b.y, z + b.z);
    }

    // 函数重载①：Vec3 * Vec3 → double（点积）
    double operator*(const Vec3& b) const {
        return x * b.x + y * b.y + z * b.z;
    }
    // 函数重载②：Vec3 * int  → Vec3（数乘）
    Vec3 operator*(int n) const {
        return Vec3(x * n, y * n, z * n);
    }

    // 类外定义（友元，传入两个 Vec3）
    friend Vec3 operator-(const Vec3& a, const Vec3& b);
    Vec3 operator+(int n) const;
};

Vec3 operator-(const Vec3& a, const Vec3& b) {
    return Vec3(a.x - b.x, a.y - b.y, a.z - b.z);
}

Vec3 Vec3::operator+(int n) const {
    return Vec3(x + n, y + n, z + n);
}