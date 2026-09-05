#include <iostream>
using namespace std;
#include <cstring> 

class String {
private:
    char* data_;
    size_t len_;

public:
    String(const char* s = "") {
        len_ = strlen(s);
        // 多分配 1 字节存放 '\0'
        data_ = new char[len_ + 1];
        strcpy(data_, s);
    }

    // 深拷贝：拷贝构造
    String(const String& other) {
        len_ = other.len_;
        data_ = new char[len_ + 1];
        memcpy(data_, other.data_, len_);
        data_[len_] = '\0';
    }
    // 深拷贝：析构函数
    ~String() {
        delete[] data_;
    }

    // 深拷贝：赋值运算符重载
    // 同时包含析构和拷贝构造的功能，但不适合直接复用，会存在问题
    String& operator=(const String& other) {
        // 1. 自赋值检查
        if (this == &other)
            return *this;

        // 2. 释放原有资源
        delete[] data_;

        // 3. 拷贝构造
        len_ = other.len_;
        data_ = new char[len_ + 1];
        memcpy(data_, other.data_, len_);
        data_[len_] = '\0';


        return *this;
    }
};

