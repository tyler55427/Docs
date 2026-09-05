# java

## 杂项

java 可以实现 double 的%运算符，而 c++不行

m%n == m-(n\*q) 其中 q 为 m%n 的整数部分

强类型：f(x=0) 报错

`System.exit(0)`使关闭窗口同时终止程序

静态方法通过类名调用，非静态方法通过对象调用

输入换行时使用`nextLine()`读取`\n`字符

`assert n == 1` assert bool 表达式

向上类型转化要保证内存都有：父类可以接受子类

`System.err.println(123)`打印错误信息，以红色字体输出，且和正常输出可能顺序不一样，随机

final 修饰引用数据类型，不能改变地址值，但能改变对象内容

main 方法调用 Main.main(null);

局部变量没有权限修饰符

文本块：三个双引号，直接对文本输出，空格和换行保留

> 可变长度参数
> 最后一个参数的类型后面，最后一个参数名的前面使用三个点
> `(double ... values)`调用方法时可以输入任意个数的参数

> 运算符重载
> java 不支持运算符重载，除了+（+=）可以

> Arrays.sort(arr,first,end)，必须实现 cmoparable 接口里面的 compareTo

final 方法不能被派生类覆盖

this 和 super 不能同时调用

#### 隐式转化

java 不允许将 double 转化为 int 类型，但 c++可以。
不过可以通过

```java
    double a = 23.4;
    int n= (int) a;
```

转化

#### for-each 循环

将数组中的每个元素放入指定变量，执行语句
缺陷：只能按顺序访问元素

```java
    for(var i : arr){

    }
```

## 1. 数据类型

1. 基本数据
2. 引用数据
   class,数组,interface,record,enum,@interface
   引用传递可以改变原来的对象
   使用 new 创建对象

## 输入

`input.next()`是到界定符
`input.nextLine()`是到\n 之前并舍弃\n

---

## 2. 数组

##### 复制

`arraycopy(arr a,int start,arr b,int index,int length)`
a 为源数组，b 为目标数组，start 为 a 的起始下标，index 为 b 的起始下标，length 为复制的个数
内存不够会抛出异常

##### 二维数组

可以通过一个维度来 new 实现不规则数组

### java.util.Arrays

1. 排序
   `.sort()`
    1. 自然排序
    2. 起始位置和终点位置排序
    3. 使用比较器排序 COmparator
2. 查找
   `.binarySearch()`
3. 拷贝
   `.copyOf()` `.copyOfRange()`
4. 比较相等
   `.equals()`
5. 将一个值填充到数组的每一个元素中
   `.fill()`

## 3. String

```java
    String str =  "hello world";
    // 返回索引
    str.indexOf();
    // 比较，大于零，小于零
    str.compareTO();
    // 连接
    str.concat("!");
    // 子字符串，从index开始
    str.substring(2);
    // 转化大写
    str.toUpperCase();
    // 比较
    str.equals(String s);
    // 比较忽略大小写
    sre.equalsIgnoreCase(String s);
    // 分割成字符串数组
    String[] str = s.split("正则表达式");
    // join方法，静态方法
    String[] temp;
    String str = String.join("-",temp);
```

##### 字符串转化为基本类型

`parseInt(String str)` 将字符串转化为整数
`parseFloat(String str)` 将字符串转化为浮点数
`parseInt("234")`  
`valueOf()` 将基本类型转化为字符串

## 4. 类

五个成员：属性，方法，构造方法，代码块，内部类
一个文件只能有一个 public 类，它的名字要和文件名一样，其他类不能用 public 修饰
创建类的数组的时候不会实例化对象，只是具有引用能力

1. JavaBean 类，用来描述一类事物的类
2. 测试类，main 方法
3. 工具类，不用来描述
    1. 私有化构造方法
    2. 方法定义为静态

#### 权限修饰符

private: 同一个类
空着不写/缺省：同一个包中的其他类
protected: 不同包的子类
public: 不同包的无关类

#### this / super

this：一个变量，当前方法调用者的地址值
super：父类的存储空间

> 在默认构造里面调用有参构造，实现默认初始化
> 必须写在第一行

#### 代码块

局部代码块
构造代码块:

1. 写在成员变量位置
2. 创建对象时会先执行构造代码块，再执行构造方法

```java
    public class p{
        private String name;
        private int age;
        // 必须要有{}
        {
            System.out.println("p被创建");
        }
    }
```

静态代码块
只执行一次，当类加载到内存时用一次
用来对类初始化，对数据也要 static 才能用

### 抽象类

只要有一个抽象，类就是抽象的
不能创建对象
抽象是子类都要有，接口是子类部分有

##### 适配器设计模式 " \*\*\*Adapter "

当不想使用接口中全部的的抽象方法的时候，可以用一个类实现接口的空实现，然后继承这个类，这个类一般也是 abstract，防止创建对象

## 内部类

内部类可以访问外部，外部想访问内部必须创建对象
内部类时 private 时，创建接受要用 Object，不能用 Outer.Inner（因为无法访问到）
内部类和外部类重名时，使用 Outer.this.a 调用外部
类内可以重新定义类和接口
内部类不能定义 static

`Outer outer = new Outer();`
`Inner inner = outer.new Inner();` 实例 outer
静态内部类的直接实例化
静态内部类想要访问外部类的非静态对象要创建外部类对象
`Outer.Inner src = new Outer.Inner();`

匿名类，只调用一次，定义的同时调用 new，继承和实现不用+extends、implement

```java
new swim();
new swim(){
    重写
};
```

```java
// Animal有一个抽象方法
method(Animal e);
method(

    // 没有名字的类继承了Animal
    new Animal(){
        @Override
        public void eat(){
            sout("eating");
        }
    };

    new Animal(){
        @Override
        public void eat(){
            sout("eating");
        }
    }.swim();

);
```

## 多态

优点：方法传递形参是父类，可以传递子类
缺点：上述传递不能调用子类的特有的方法

> 解决：将调用者类型强制显示转化为子类，前提是调用者原本的类型要有子类的类型
> 做类型判断，再转化`A instanceof B`
> 新特性：`A instanceof B b`判断的同时，直接转化

变量：编译看左边，运行看左边
方法：编译看左边，运行看右边
编译是否报错
容器可以添加任意类型，object 的终极父类

## 5. 接口

接口是引用类型
接口作为形参传入可以调用实现了接口的类

1. 变量都是 public static final（可省略），要再接口内初始化
2. 方法都是 public abstract（可省略）
   只有声明，没有实现
   要重写实现，实现的时候要加上 public
   可以被继承
   直接在接口里写实现
3. 方法也可以是 public static/default (多个接口有相同方法要重写，重写时再重写的地方不用加 default 关键字)
4. 定义私有方法
5. 静态私有 static private ，接口内调用实现封装
    > 例子
    > 比较类实例对象的大小比较
    > `compareTo()` 一个参数
    > 排序
    > `comparable()`两个参数
    > compare();

### 虚方法表

非 private、static、final
Object 有 5 个虚方法
方法重写，快速查找，防止多重继承导致运行速度

##### 重写

重写可以覆盖相同的虚方法表，否则根据作用域不同，会有两个相同名字的虚方法
注意事项

1. 子类的访问权限必须大于等于父类
2. 返回值类型必须小于等于父类
3. 不能加到虚方法表的方法不能重写

## 6. 初始化

1. 声明时初始化
2. 使用初始化块（静态变量使用静态初始化块）

```java
    // 静态
    // 只能使用静态变量
    public class test{
        static int x = 23;
        static{
            x = 12;
        }
    }
```

3. 使用构造方法初始化
   顺序：1. 默认值 或 初值初始化 2. 初始化块 3. 构造方法

### 7. 命令行参数

通过命令行调用时能够接受输入的参数，通过 args[i]输出

```java
    System.out.println(args[0]);
    System.out.println(args[1]);
    System.out.println(args[2]);
```

## 8. 静态工厂

构造方法是私有的时候，通过调用静态方法调用私有的构造函数

1. 限制创建对象为固定值
2. 实现单例，只创建一个对象，当创建多个对象时，实际上只是引用了同一个对象

### 9. package

import static 导入静态直接用
同一个包不用 import
同时使用两个包的同名类使用全类名

## 10. 异常

{
java.lang.Throwable

1. Error(系统级别的错误，硬件)
2. Exception
    1. RuntimeException
    2. 其他异常（编译异常）
        > throws，将异常从该方法抛出到调用该方法的方法（回溯），找是否有异常处理，没有就一直到 main 方法交给虚拟机处理
        > 可以在 catch 中继续向上抛出异常

#### Throwable 的常用方法

第三个常用，包含前两个
`public String getMessage();`返回 Throwable 的详细信息字符串
`public String toString();`返回可抛出的简短描述
`public void printStackTrace();`把异常的错误信息输出在控制台

##### 作用：

1. 查询 bug 的关键参考信息
2. 作为方法内部的一种特殊返回，通知底层的执行情况

#### 处理方式

##### 默认虚拟机处理

    输出在控制台，而且程序停止

##### 捕获异常

出现异常时可以让程序继续往下运行

```java
    try{
        可能出现异常的代码
    }catch(异常类名 异常变量名){
        异常的处理代码
    }catch{

    }
```

```java
    // 存在相同的异常处理的时候（JDK7）
    try{
        可能出现异常的代码
        // 同时捕获多个异常，只能用一个|来捕获
        // 处理的代码相同的时候
    }catch(异常类名 异常变量名 | 异常类名 异常变量名){
        异常的处理代码
    }finally{

    }
```

```java
    // try-with-resources
    // 在异常被捕获前，将资源回收
    try(Person p = new Person()){

    }catch(Exception e){

    }
```

##### finally

> finally 的代码总是会执行
> 用于异常出现导致程序停止后，资源的释放、文件的关闭

1. try 没有问题
   正常执行 try，不执行 catch
2. try 遇到多个问题
    1. 写多个异常来捕获
    2. 多个异常出现父类子类的关系的时候，父类要出现在子类的下面（从上往下依次匹配）
3. try 中遇到的问题没有被捕获
   虚拟机默认捕获异常，并且代码不继续执行
4. try 中遇到了问题，try 下面代码是否执行
   不会执行，直接跳转到对应的 catch

##### 抛出异常

1. throws
   写在方法定义出，声明一个异常，告诉调用者可能会出现哪些异常
   程序停止

```java
    public void test() throws 异常类名1,{

    }
```

编译时异常必须手动写上
运行时异常可以不写 2. throw
写在方法内，用来结束方法，手动抛出异常对象，交给调用者处理，方法中的代码不执行

```java
    public void test(){
        throw new NullPointrException();
    }
```

### 自定义异常

1. 定义异常类
2. 写继承关系
   编译异常继承 Exception
   运行异常继承 RuntimeException
3. 空参构造和带参构造

}

## 11. 断言

默认没有打开，JVM-ae
assert + 布尔表达式 : 输出结果
断言失败，抛出 Error

## 12. 类的其他使用

1. 记录
   将类声明中的 class 换成 record
   成员变量都是 final,private 类型
   将成员变量作为形参，JVM 自动提供变量名的访问，但不提供修改
   里面可以有静态变量
2. 枚举
   继承了抽象类
   name 名字
   ordinal 序号
3. 注解类型
   特殊的接口
   值为键值对，只有一个键值对可以不用 key 值
   @Override、@Deprecated（弃用）、@SuppressWarnings（取消警告）`@SuppressWarnings( value = {"uncheck","deprecation"} )`

自定义注解，可接口的定义一样

```java
    public @interface My_ZhuJie{
        int major() default 1;
        int minor() default 0;
    }
    @test(major = 1, minor = 0)
    public class test{

    }
```

## 13. 泛型

类、接口都可以是泛型

```java
    public class Node<T>{

    }
    public interface Read<T>{

    }
```

泛型方法必须在方法返回值前指定泛型

```java
    public static<T> T f(T x){
        return x;
    }
```

泛型传入的参数是类的时候，类之间没有继承关系，为了跟多态类似，使通配符?

```java
    public class test{
        public<?> void temp(<?> t){
            return 1;
        }
        // ? 可以指定上下界
        // 上界
        public <?extends Object> void temp1(List<? extends Object> t){
        }
        // 下界
        public <?super Interge> void temp2(List<? super Interge> t){
        }
    }
```

> 类型擦除
> 例如：`Node<Interge> 被转化成 Node`

```java
    public class MyClass<E>{
        public static void myMethod(Object item){
            if(item instanceof E) // 编译错误
            E item2 = new E(); //编译错误
        }
    }
```

## 14. 文件

方法

```java
    boolean exists(); // 对象是否存在
    long length(); // 返回指定文件的字节长度，不存在返回0
    boolean createNewFile(); // 文件不存在时，创建一个空文件，返回true，否则返回false
    boolean renameTo(File newName); // 重新命名指定的文件对象，正常重命名返回true
    boolean delete(); // 删除指定的文件。若为目录，则目录为空才能删除
    long lastModified(); // 返回文件最后被修改的日期和时间，计算毫秒数
```

文件分为文本文件和二进制文件

### 二进制

InputStream 和 OutputStream
实现了 java.lang.AutoClosable 接口，可以在 try-with-resources 使用，自动关闭

```java
    int read()
    int read(byte[] b)
    void close()

    void write(int b)
    void write(byte[] b)
    void close()
    // 构造方法
    FileInputStream(String name)
    FileInputStream(File file)

    FileOutputStream(String name)
    FileOutputStream(String name,boolean append) // append为true，则从文件末尾开始书写
    FileOutputStream(File file)
```

### Buffer

```java
    // 构造方法
    BufferedInputStream(InputStream in)
    BufferedInputStream(InputStream in,int size) // size指定缓冲区大小,默认512字节

    BufferedOutputStream(InputStream out)
    BufferedOutputStream(InputStream out,int size) // size指定缓冲区大小
```

### Data

```java
    // 构造方法
    DataOutputStream(OutputStream outstream)
    DataInputStream(InputStream instream)
```

### 文件加密

使用异或，因为两次异或可以变回原样

## 15. 函数式编程

### lambda 表达式

### 预定义函数接口

```java
    Comsumer<T> //带一个参数不返回结果
    public interface Conusmer<T>{
        abstract void accept(T t);
        default void andThen(){
            // 默认方法
        }
    }
    Supplier<T> //结果的提供者
    public interface Supplier<T>{
        abstract T get();
    }
    Predicate<T> //返回boolean
    public interface Predicate<T>{
        abstract boolean test(T t);
    }
    Functioin<T,R> //返回结果和传入参数不同
    public interface Function<T,R>{
        abstract R apply(T argument);
    }
    BiFunction<T,U,R> //两个传入参数，也是apply方法
    UnaruOperator<T> //一个操作数的运算，结果和操作数类型相同
    BinaryOperator<T> //有两个操作数的运算
```

### 方法引用

许多方法是带有一个函数式接口对象作为参数。如果传递的表达式有实现的方法，可以使用一种特殊的语法，方法引用代替 lambda 表达式
?适合返回值直接是调用另一个函数的

## 16. Stream

就像一个管道，分为顺序流和并行流，并行流支持多核

### 创建流

Stream<int> stream = Stream.of();

1. Stream.of()
   用于生成长度固定，元素确定的数组
2. Stream.generate()
   动态生成内容，每次生成的内容不同，例如随机数
   生成的是无限流，可以通过 Stream.generate().limit(10)来限制元素个数
3. 使用其他容器转化
    1. var n = Arrays.stream(name);
    2. List<int> list = List.of(1,2); var l = list.stream();
       使用容器转化的好处是，当 stream 被终端操作消耗后，可以继续通过容器构造相同的 stream

```java
    of() // 根据给定值返回一个流
    concat() // 连接两个流，返回流
    distinct() // 使用equals()方法比较流元素对象，跳过重复项
    sorted() // 返回自然顺序排序的一个新流
    forEach() // 在流的每一个元素执行操作
    count() // 返回个数
    empty() // 创建并返回一个空流
    filter() // 返回一个新流，元素是给定谓词匹配的元素（过滤）
    limit() // 返回一个新流，元素的数目是给定的最大数量
    map() // 返回一个流，包含应用一个给定函数的结果元素
    max() // 返回最大
    min() // 返回最小
    reduce() // 使用一个标识和一个累加器在流的元素上执行规约操作
    toArrays() // 返回包含流中所有元素的数组
    connect(Collectors.toList()) // 终止操作
```

### 有些方法执行中间操作，有些方法执行终止操作。

1. 终端操作（如 forEach、collect、reduce 等）会消费流，流在操作后关闭，不能再次操作。
2. 中间操作（如 map、filter、sorted 等）返回一个新的流，允许链式调用。
3. 每次需要对数据执行新的操作时，重新创建一个流对象。

### 一次操作原因

1. 一次性遍历数据源
   流背后的核心理念之一是一次性遍历数据源。这意味着流在处理数据时，会逐个处理每个元素，一旦遍历完成，流就不能再重用。终端操作会触发对数据源的遍历并执行相应的操作。

2. 惰性求值和即时求值
   流的中间操作是惰性求值的，只有在需要终端操作时才会执行实际的计算。而终端操作是即时求值的，它们会触发所有惰性操作，并执行计算。这使得一旦执行终端操作，流的全部数据就已经被处理和消耗，流也就完成了它的使命。
   流操作时延迟的，在源的计算只有当终止操作开始时才执行。

3. 资源管理和性能优化
   通过设计为一次性使用，流的实现可以更高效地管理资源。流处理过程中可以优化内存和性能，因为它们可以释放在处理过程中分配的任何资源（如迭代器、文件句柄等），避免资源泄漏。

4. API 设计和易用性
   流的设计也考虑了 API 的简洁性和易用性。强制流在终端操作后被消耗，避免了可能的混淆和错误，确保开发者不会无意中尝试对已消耗的流进行进一步操作。

## 17. 数据库 DBS

数据库语言 SQL

1. 数据定义语言 DDL

2. 数据操作语言 DML

### 连接池

不用考虑关闭文件和抛出异常的问题

### DAO 设计模式

应用程序访问数据库，建立连接

### 可滚动和可更新的结果集

## 18. 多线程

进程、线程

### 并发操作

原子操作
java.util.concurrent.atomic
连接池，线程池。用空间换时间，解决创建和消除消耗的时间。

### 线程锁

## 19. 网络编程

Socket 类
端口，一般的服务在 1024 以下，自己创建尽量在 1024 以上
TCP 传输协议
有链接，可靠
双向通道，传输数据没有大小限制
UDP 协议
无连接，不可靠
因为无连接，每个数据报不能超过 64k，但可以有多个数据报

### TCP

ServerSocket(int port)
ServerSocket(int port,int queue)最大连接数
Socket()构造函数，用来连接已经创建的服务器端口

### UDP

DatagramSocket(int port)创建端口
receive(DatagramSocket p)
send(DatagramSocket p)
getInetAddress()
getLocalAddress()

DatagramPacket(byte[] buf,int length)接受数据之前，要创建这个对象，用来接收数据的缓冲区及长度
DatagramPacket(msg,send.length(),clientIP,clientPort)发送同理
socket.send(packet)

## 进阶

Spring Boot
Spring Cloud
前端
