# C++

万能头<bits/stdc++.h>

## 杂项

### C 语言和 C++的区别

C 语言的函数声明没有参数必须要显式声明 func(void)（好像不影响）

> 单定义：当一个文件定义了变量，外部文件引用使用`extern`，且不能初始化值
> 有外部变量但不使用，新定义用`static`覆盖外部变量

> 下面代码片段意味着仅当以前没有使用预处理器编译指令#define 定义名称 STRING*H* ，才处理语句
> #ifndef STRING*H*
> #define STRING*H*
> #endif

命名空间和函数不能再代码块里面

相同的内存块，重复导入会冲突

struct 的内容全是 public

typedef int T 类似于 `template <class T>`

将构造函数写在 private 防止 main 创建对象

函数重写实现，有 const 要加 const，不然就相当于重新定义了一个函数
`virtual void temp()const`
`void temp()const`

-nan 是出现无效的数学运算，例如除以 0

## 1. 命名空间和作用域

```C++
    int main(){
        int a;
        {
            int a; //覆盖
        }
    }
```

```C++
int b;
namespace B{
    int b;
}
int main(){
    cout << B::b << endl;
}
```

using namespace B;
定义全局变量和命名空间中的变量重名时，不能通过 using namespace 调用，要使用作用域解析符调用 B::b;

## 2. 枚举

class 的 enum 成员跟 static 一样
当 enum 中的内容冲突时可以将 enum 定义为 class，使作用域分开，防止冲突
enum 是 int 类型，不能是 double
enum 可以转换为 int，但 int 不能转化为 enum

> 范围
> 大于 max 的$2^n$-1，没有的值为上一个+1

### 3. 符号重载

`c = a + b`
`c = a.operator+(b)`（一定成立）

#### 4. 转换函数

1. 类方法
2. 无返回
3. 无参数

```C++
operator int()const{
    //手动显示转化返回
    return int(x+0.5);
}
```

## 5. 类

class 不支持隐式转换，但可以显示转化
支持向上转换，也可以通过指针转换类型赋值

> 指针
> 只有共有派生类才能兼容基类类型，实现函数多态访问派生类的基类（遵循：防止指针访问无效内容）
> 基类指针作为形参传入时，只能调用基类成员函数--因为静态编译，编译阶段确定指向了基类的成员函数

编译器会尝试将在类内实现的函数变成 inline，但如果函数长则不会
const 成员函数类都可以调用，但 const 修饰的只能调用 const 成员

#### 重载-Overload

1. 相同的作用域
2. 函数名字相同
3. 参数类型（包括 const 指针 或 引用） ， 顺序 或 数目不同

#### 覆盖-Override

修改基类函数定义（和虚函数有关）

1. 重新定义基类的方法，应保持和原来的原型完全一样。
2. 但如果返回类型是基类的引用或指针，则可以修改为指向派生类的引用或指针只适用于返回值

```c++
    class base{
        virtual base& build(int n);
    };
    class derived: public base{
        virtual derived& build(int n);
    };
```

##### virtual 和重载

1. 在派生类中重新定义某个重载版本时，为了避免隐藏基类的其他重载版本，可以使用 using 声明显式引入基类的所有重载版本。
2. 或者在派生类中重新定义所有的基类版本。
3. 如果没有显式引入基类的所有重载版本，那么基类中的那些版本将被隐藏，派生类对象将无法调用它们。
4. 可以通过在派生类中调用基类版本的方式来改变其中的一个版本，同时保留基类的其他版本。

#### 隐藏-Overwrite / hide

1. 派生类的函数和基类函数同名，但是参数列表有所差异
2. 派生类的函数和基类函数同名，参数列表相同，但是基类函数没有 virtual 关键字

```c++
    void base::build(int n);
```

### 继承

没有被覆盖或隐藏的基类函数，包括在基类中重载的函数
可以用

```C++
    class BB:public AA{
        private:
            // show是函数指针，没有（）
            using AA::show;
    };
```

使得某个具体的继承降低权限，但不能通过这个来升高权限

**！！注意！！**
连续继承时，必须在构造函数的参数列表把基类都写上，即使中间类的构造函数已经在参数列表里写了基类的构造函数。

##### 菱形继承

菱形继承会使一个基类被派生了两次，导致重复继承
重复继承时，在继承的语法+virtual，使只继承一次（对会被继承两次的类的继承的时候使用 virtual）

虚基类的构造函数调用优先于其他基类的构造函数

只能被初始化一次，只有一次调用构造函数的输出

但派生类继承相同一个基类时，两个派生类的基类的地址时不同的；而虚继承，两个派生类的基类的地址是相同的

### 虚函数和纯虚函数

纯虚函数又称为 ABC
可以将函数声明为抽象，没有 virtual
`void Move(int x)`

派生类重写虚函数可以+virtual，增加可读性。（不论派生类是否有关键字，它都是虚函数）

virtual 必须在声明的时候加上

函数传参 和 类创建 的时候，只有是 **基类的指针** 和 **引用** 才能实现多态，否则只是隐藏，会调用基类的成员函数

虚函数的**返回值**可以不同，但只能在基类和派生类的指针中选择

虚析构，根据对象具体是什么类型，调用对应的虚构函数

类外可以写纯虚函数的实现

派生类可以覆盖基类的虚函数变成纯虚函数

如果建立 vtable 表（虚方法表），则所有函数都要实现，否则会 `undefined referrence`（经常出现的报错）

包含虚函数的基类的析构函数必须是公开且虚，或者在保护且非虚

typeid().name() 包含头文件 `<typeinfo>` 使用**指针**的虚函数的时候能够判断类到底属于哪个类型，类似 instanceof

增加 final 可以使继承终止，

可以在成员函数加
`void temp() final`
可以在类加
`class Temp final {};`

## 6. new

`new(3)` 三个字节
`new int(3)` 创建一个 int 类型，值为 3
`new int[3]` 创建三个 int 类型，即数组
char* str 类型的字符串，创建 new char[strlen(str)];
char* 类型，使用 C 语言的字符串数组的函数

new 类型[]{初始化列表}
都可以用{}作为参数的初始化，例如：int a{3};

**总结**

1. 指针可以是单独的一个数据，也可以是这个数据类型的数组
2. 双重指针可能是二维数组，也可能是存放指针的一维数组，而指针是指向一个 new 出来的对象

## 7. 转化

#### 隐式转化

1. non-const -> const
2. char->int , float->double
3. int->double , double->int
   定义 P(long);
   定义 P(double);
   P(int)会产生二义性，int 两种类型都可以隐式转换

函数调用的时候，如果没有引用，会复制一份，这个时候会将 const -> non-const 。如果引用的话，对于字面量"123"必须是 const，才能正确传入，因为不允许将原本的 const -> non-const

#### 转换检查

1. static_cast<>

做类型转换检查，编译时报错

但是只要相关就可以转换，例如：将原本就是父类的类型转换为基类类型，即使没有内存也不会报错

会对内存进行改变，例如：将 char 转换为 int 会将字节数扩大

2. dynamic_cast
   动态检查，必须有 virtual
   失败返回空指针
3. const_cast
   只能用于指针和引用
   只能改变只读，不能改变常量，但是语法可以，运行未定义
4. reinterpret_cast
   和第一个类似，但是不改变内存值
   uint16_t----16 个位字节

## 8. 指针

NULL 是 (void*)0 可以作为 int，也可以作为 int* 传入。也就是说，可以将指针赋值为 0。
nullptr 只能作为 int\* 类型传入

## 9.模板

模板不能单独编译，必须和实例化一起使用

泛型时静态，但编译器不编译，函数调用的时候实例化代码调用

不显式指定，不会发生隐式类型转化，如果调用会报错

### 函数模板

```c++
    template<class T>
    void print(T v){
        cout << v << endl;
    }
    // 特化
    // 如果将全部模板参数都特化了，则可以直接当作普通函数
    template<>
    void print(int v){
        v++;
        cout << v << endl;
    }
```

调用顺序；普通函数->特化->模板->发生隐式类型转化后调用正常函数

### 类模板

类声明中定义方法，省略模板前缀和类限定符；类模板类外实现要加上模板模板前缀和模板

模板前缀：Temp<T>:: 、 模板限定符：template<class T>

实例化类模板时，**必须**显示指定模板，不能通过构造函数自动推导

模板类和类模板：类模板是类的一个模板，模板类是具体指定了类型后的类

类模板的不同实例化版本是不同的类，如果有静态成员，则都有一份

显示指定，只是实例化了类，成员函数没有实例化

可以递归调用模板，比如 vector 递归调用实现二维数组

类模板参数可以有默认值

包含编译模式
定义和实现都在.h 文件

### 非类型的模板形参

模板内部的常量，编译时确定，一般为 int、可以转化为 int 的 char 等。
模板中不能对参数进行修改和取地址

```c++
    template<classT,int N>
    void print( T (&arr)[N] ){ // T (*arr)[N] , 不用指定N
        for(int i=0;i!=N;++i){
            cout << arr[i] << endl;
        }
    }
    template<class T>
    void print( T* arr ,int n){
        for(int i=0;i<n;++i){
            cout << arr[i] << endl;
        }
    }

    int intArr[6] = {1, 2, 3, 4, 5, 6};
    double dblArr[4] = {1.2, 2.3, 3.4, 4.5};

    template <typename T, int N>
    void print(T (&arr)[N]) {
        // 直接传入数组名的时候调用
	    cout << "(T&)[" << N << "]\n";
    }
    print(intArr);

    template <typename T, int N>
    void print(T (*arr)[N]) {
        // 传入数组名取地址的时候调用
    	cout << "(T*)[" << N << "]\n";
    }
    print(&intArr);
```

### 具体化

#### 1. 隐式实例化

主要使用方式
只有在真正要生成对象的时候才会生成类定义，并具体化

#### 2. 显式实例化

没有创建对象就会生成类定义，但只有调用的时候才生成具体化

```c++
    // 显式实例化
    template void print<int>(int)
    template void print<>(char)
    template void print(double)

    // 成员函数也会实例化
    template class Person<int>;
```

#### 3. 显示具体化，又叫特化

特化，用于某一个类型的代码逻辑不同的时候

```c++
template<typename T>
class MyClass {
public:
    T value;
    MyClass(T val) : value(val) {}
    void print() {
        std::cout << "Value: " << value << std::endl;
    }
};

// int的特化
template<>
class MyClass<int> {
public:
    int value;
    MyClass(int val) : value(val) {}
    void print() {
        cout << "Integer Value: " << value << endl;
    }
};
```

#### 4. 部分具体化

```c++

template<typename T, typename U>
void myFunction(T t, U u) {
    std::cout << "First argument: " << t << std::endl;
    std::cout << "Second argument: " << u << std::endl;
}

template<typename T>
void myFunction(T t, int u) {
    std::cout << "Partial specialization for when U is int" << std::endl;
    std::cout << "First argument: " << t << std::endl;
    std::cout << "Second argument: " << u << std::endl;
}
```

模板的友元

1. 非模板友元
   模板的所有实例化的友元
2. 约束模板友元
   友元函数本身成为模板
    1. 类定义的前面声明每一个模板函数
       类定义友元要找到模板函数，但因为没有定义类，又不能写具体实现
    2. 在类里面将模板声明为友元
    3. 为友元提供模板定义
3. 非约束模板友元

```c++
    template<class T>
    class Person{};
    void Person<T>::test(){}

    template <class T>
    class TX {
    public:
        T a;
        // 模板内的友元，类内实现，类可以使用相同的模板参数
        friend void get(TX<T> t){
            cout << t.a << endl;
        }

        // 模板内的友元，类外实现要使用不同的模板参数
        template<class U>
        friend ostream& operator<<(ostream&, TX<U> tx);
        // 否则，就得显示指定
        friend ostream& operator<<(ostream&, TX<int> tx);
};

```

## 10. lambda

[捕获列表](参数列表)->返回类型{函数体}
空参，参数列表可以省略
一般可以自动推导返回类型，“->返回类型”可以省略
捕获列表可能是一些常量？

每个方法的参数列表可能有**固定的格式**

例如：accumulate 的第一个参数 sum 表示累计计算的结果，第二个参数表示从容器中获取的元素

## 11. 异常

exception 的构造没有有参构造
其他异常的构造没有默认构造，只有传入参数（要打印的错误信息）的构造函数

throw 可以抛出任何类型的对象，同时用相应的类型进行捕捉

catch **不支持**隐式类型转化，按顺序进行匹配

异常的 catch 一般使用引用，否则回由于复制出现像虚函数类似的错误

可以通过直接 throw;将异常再次抛出，交给调用者处理
可以使用 catch(...)捕获所有的异常
异常通过重写虚函数 waht()来打印错误信息

捕获异常的时候，如果不需要用到异常的变量，可以捕获的时候不写异常的变量名

c++11 新增，但是在 c++17 又删除的：在调用的地方声明这个函数会抛出什么类型的异常，这时，如果函数里面出现的异常不在上述声明里面，则直接调用 abort()，最终的崩溃函数
如果声明的是 nonexcep，则不允许这个函数抛出异常，如果出现异常，直接调用 abort()
捕获到异常，再次将其抛出的时候，如果没有使用引用传参，则 catch 中对捕获的异常处理无效，直接抛出接受到的异常

### 自定义异常

继承 exception，重写里面的虚函数 what()
构造函数的时候，要重载**两种字符串**形式（char\* string），同时还要**加上** explicit，保持异常不支持隐式转化的标准

如果在构造函数里面出现异常，则这个对象没有被真正创建，不会创建空间，不会被析构，所以有内存泄漏的风险

# 变量初始化

全局变量、静态变量自动初始化

局部变量、动态分配不会自动初始化
