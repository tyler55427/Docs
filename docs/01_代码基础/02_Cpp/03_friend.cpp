#include <iostream>
using namespace std;

// ===== 1. 全局函数作友元 =====
class Room {
public:
    Room(int sqm) : area(sqm) {}
    // 声明友元
    // 虽然是全局，但是需要在类中声明
    friend void inspect(Room& r);
private:
    int area;
};

void inspect(Room& r) {
    
}

// ===== 2. 成员函数作友元 =====
class Room2;
class Door {
public:
    // Door 的成员函数作 Room2 的友元
    // 声明Room2类的前向声明
    void open(Room2& r);
};

class Room2 {
public:
    Room2(int sqm) : area(sqm) {}
    friend void Door::open(Room2& r);
private:
    int area;
};

// ===== 3. 类作友元 =====
class Room3 {
public:
    Room3(int sqm) : area(sqm) {}
    friend class Manager;  // 整个 Manager 类都是友元
private:
    int area;
};

class Manager {
public:
    void manage(Room3& r) {
        cout << "3. 类友元访问: " << r.area << " 平米" << endl;
    }
};
