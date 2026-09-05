# C

## 一、函数与递归

- 函数基础

```c
int add(int a, int b) {
    return a + b;
}

void foo(void);   // 明确无参
```

- C 语言**传值调用**：修改形参不影响实参。若要修改实参，必须传**指针**。

```c
// 正确：通过指针交换
void swap(int* a, int* b) {
    int t = *a; *a = *b; *b = t;
}
```

---

## 二、作用域与存储类别

- 局部变量

| 类型         | 说明                         |
| ------------ | ---------------------------- |
| `auto`     | 默认，函数返回后销毁         |
| `static`   | 函数返回后保留值，跨调用持久 |
| `register` | 建议放在寄存器中             |

```c
int counter() {
    // 首次初始化，之后跳过，不会报错
    static int count = 0;  
    return ++count;
}
```

- 全局变量

```c
int GlobalVar;           // 自动初始化为 0
static int FileVar;       // 仅本文件可见
extern int ExtVar;       // 引用其他文件定义
```

- 多文件编译

```
.c 文件 ──编译──> .o 文件 ──链接──> 可执行文件
```

```bash
## 分别编译后链接
gcc -c main.c -o main.o
gcc -c func.c -o func.o

## 一步到位
gcc main.c func.c -o prog
```

- `##pragma once`：确保头文件只展开一次
- 自定义头文件用 `""`，系统头文件用 `<>`

---

## 三、数组

- 一维数组

```c
int arr[10];              // 未初始化
int arr[10] = {0};       // 全部为 0
int arr[10] = {1, 2, 3}; // 前三个为 1,2,3，其余为 0
int arr[] = {1, 2, 3};   // 自动推导长度为 3

// C99 变长数组（VLA）
int n = 10;
int arr[n];
```

- 二维数组

```c
int mat[3][4];

// 按行初始化
int mat[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};

// 按顺序初始化
int mat[3][4] = {1,2,3,4,5,6,7,8,9,10,11,12};

// 省略第一维
int mat[][4] = {1,2,3,4,5,6,7,8,9,10,11,12};

// 部分初始化
int mat[3][4] = {{1}, {5,6}, {0,0,11}};
```

- 数组作为函数参数

```c
void sort(int a[], int n);          // 等价于 int*
void matrix_add(int a[][3], int b[][3], int m);
```

---

## 四、指针

- 指针基础

```c
int a = 10;
int* p = &a;    // 取地址
*p = 20;        // 解引用
```

- NULL 指针

```c
int* p = NULL;
```

- 指针算术

```c
int arr[6] = {0,1,2,3,4,5};
int* p = arr;

p++            // 指向下一个元素
p + 3          // 指向后第 3 个
q - p          // 元素个数距离
```

- 指针与数组

```c
int arr[5] = {10,20,30,40,50};
int* p = arr;

// p[i] 等价于 *(p + i)
// arr[i] 等价于 *(arr + i)

for (int* q = arr; q < arr + 5; q++)
    printf("%d\n", *q);
```

- const 与指针

```c
const int n = 10;
const int* p1 = &n;     // 指向的内容不可修改
int* const p2;           // 指针本身不可修改
```

- void\* 泛型指针

```c
void* memcpy(void*, const void*, size_t);
void* malloc(size_t);
```

- 数组指针 vs 指针数组

```c
int m[3][4];

int (*p)[4] = m;    // 数组指针：指向 int[4]
int* arr[3];          // 指针数组：3 个 int* 的数组
```

---

## 五、字符与字符串

- ASCII 码

  - 控制字符：0~31（如 `\n`=10, `\r`=13）
  - 可打印字符：32~126
  - 数字 `'0'~'9'`：ASCII 48~57
  - 大写字母 `'A'~'Z'`：ASCII 65~90
  - 小写字母 `'a'~'z'`：ASCII 97~122
  - 字符分类函数（ctype.h）

```c
isalnum(c)  isalpha(c)  isdigit(c)
islower(c)  isupper(c)  isspace(c)
tolower(c)  toupper(c)
```

- 字符串概念

字符串是以 `'\0'` 结尾的字符序列。

```c
// 不是字符串（没有 '\0'）
char msg[3] = {'H', 'i', '!'};

// 是字符串
char msg[4] = {'H', 'i', '!', '\0'};
char msg[] = "Hi!";
```

- 字符串输入输出

```c
char name[64];
scanf("%s", name);              // 遇空白字符停止，不需要 &
fgets(buf, sizeof(buf), stdin); // 读取一行
printf("%s", str);
puts(str);
```

- 常用字符串函数（string.h）

```c
strlen(s)           // 长度（不含 '\0'）
strcpy(dest, src)  // 复制
strncpy(dest, src, n)  // 复制前 n 个
strcat(dest, src)  // 连接
strcmp(s1, s2)      // 比较，返回 <0/0/>0
strchr(s, c)        // 查找字符
strstr(s1, s2)      // 查找子串
strlwr(s) / strupr(s)  // 转小写/大写

memcpy(dest, src, n)   // 复制 n 字节
memset(s, c, n)       // 填充
```

- 字符串字面量

```c
char* s = "Hello";     // 指向只读代码段，不能修改
char t[] = "Hello";    // 数组复制，可以修改
```

---

## 六、结构体

- 定义与初始化

```c
struct Student {
    char id[6];
    char name[16];
    int age;
};

struct Student s1 = {"0101", "anna", 20};

// typedef 简化
typedef struct {
    char id[6];
    int age;
} Student;
```

- 结构体嵌套

```c
struct Address {
    char area_id[6];
    char detail[64];
};

struct Student {
    char id[6];
    struct Address home;  // 嵌套
};
```

> 结构体不能嵌套自身类型（递归定义用指针）。

- 内存布局

结构体按成员顺序连续存储，因对齐产生填充：

```c
struct A {
    char a[3];  // 3 字节
    int b;       // 填充1字节后存放
    short c;     // 2 字节
};  // sizeof = 8

// 紧凑模式
##pragma pack(1)
struct B { ... };  // sizeof = 9
##pragma pack()
```

- 成员访问

```c
struct Student s = {"0101", "anna", 20}, *p = &s;

s.age = 21;
p->age = 22;      // 推荐
(*p).age = 22;    // 等价

s = t;             // 整体赋值
```

- 结构体作为函数参数

```c
// 传指针：推荐
void print_student(const struct Student* st);

// 传值：开销大
void print_student(struct Student st);
```

---

## 七、共用体（Union）

多个成员共享同一段内存，大小为最大成员：

```c
union Number {
    int x;
    double y;
};

union Number n;
n.x = 100;
printf("%d %lf\n", n.x, n.y);  // y 值不可预测
```

---

## 八、位域

```c
struct Flags {
    unsigned int t1 : 10;  // 位宽10
    unsigned int t2 : 11;  // 位宽11
    unsigned int t3 : 11;  // 位宽11
};  // 总共32位 = 1个int
```

- 相邻位域打包拼合
- 匿名位域 `:` 跳过若干位
- 位宽为0的匿名位域强制对齐到下一个整数
- 位域不能取地址

---

## 九、枚举

```c
enum Color { RED, GREEN, BLUE };       // 从0开始
enum Status { ERR_OK = 0, ERR_FAIL }; // 显式赋值
enum Week { MON = 1, TUE, WED, THU, FRI, SAT, SUN }; // 1~7

enum Color c = RED;
c = GREEN;
int i = c;  // 可隐式转为 int
```

---

## 十、动态内存

```c
##include <stdlib.h>

int* p = (int*)malloc(sizeof(int));
free(p);

int* arr = (int*)malloc(n * sizeof(int));
free(arr);

int* q = (int*)calloc(n, sizeof(int));  // 分配并初始化为 0
int* p2 = (int*)realloc(p, new_size);
```

常见错误：内存泄漏、双重释放、使用已释放内存。

---

## 十一、预处理

- 宏定义

```c
##define MAX 100
##define SQUARE(x) ((x) * (x))
##define LEN(arr) (sizeof(arr) / sizeof((arr)[0]))
```

- 防止重复包含

```c
##pragma once
// 或
##ifndef HEADER_H
##define HEADER_H
##endif
```

- 条件编译

```c
##if defined(DEBUG)
    // ...
##endif
```

---

## 十二、文件操作

- 文件类型
- **文本文件**：ASCII 字符序列
- **二进制文件**：字节序列，内存数据直接写入
- 四步骤

```c
FILE* fp = fopen("data.txt", "r");
if (!fp) { perror("fopen"); return -1; }
// 读写...
fclose(fp);
```

- 打开模式

| 模式    | 说明                 |
| ------- | -------------------- |
| `r`   | 读                   |
| `w`   | 写（不存在则创建）   |
| `a`   | 追加                 |
| `r+`  | 读写                 |
| `w+`  | 读写（不存在则创建） |
| `a+`  | 读和追加             |
| 加`b` | 二进制               |

- 读写函数

```c
// 格式化
fprintf(fp, "%s %d\n", name, age);
fscanf(fp, "%s %d", name, &age);

// 逐字符
fgetc(fp)    fputc('A', fp)

// 逐行
fgets(buf, sizeof(buf), fp);   // 含换行
fputs("hello\n", fp);

// 二进制
fread(&st, sizeof(Student), 1, fp);
fwrite(&st, sizeof(Student), 1, fp);
```

- 文件位置

```c
fseek(fp, offset, origin);
// origin: SEEK_SET(0), SEEK_CUR(1), SEEK_END(2)

ftell(fp);    // 当前文件位置
rewind(fp);   // 重置到开头
```

- feof / ferror

```c
while (!feof(fp)) { ... }    // 判断是否到达文件末尾
ferror(fp)                    // 是否有读写错误
```

- 标准流

```c
stdin   stdout   stderr
```
