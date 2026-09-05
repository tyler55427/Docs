# KMP

**问题描述**：在文本串 s 中查找模式串 pat 的所有出现位置。

**解法**：KMP。利用已匹配的前缀信息，避免重复比较，实现 O(n+m) 时间复杂度。预处理构建 nnext 数组记录模式串的最长相等前后缀长度。

## 全局变量

nnext[i] = 模式串 pat[0..i] 的最长相等前后缀长度。例如 "ABA" 的 nnext[2] = 1（"A"）。

```cpp
vector<int> nnext;
```

## 构建 nnext 数组

模式串自我匹配，维护两个指针 i（前缀）、j（后缀）。j 指向当前要计算的位置，i 维护前缀长度。

```cpp
void buildnnext(const string& pat)
{
    int m = pat.length();
    nnext.assign(m, 0);
    int i = 0, j = 1;
    while(j < m)
    {
        if(pat[i] == pat[j])
        {
            nnext[j] = i + 1;
            ++i;
            ++j;
        }
        else if(i == 0)
        {
            ++j;
        }
        else
        {
            i = nnext[i - 1];
        }
    }
}
```

## KMP 匹配

在文本串 s 中查找模式串 pat，返回首次匹配位置（未找到返回 -1）。i=文本串指针，j=模式串指针。

```cpp
int kmpSearch(const string& s, const string& pat)
{
    int n = s.length(), m = pat.length();
    if(m == 0) return 0;

    int i = 0, j = 0;
    while(i < n && j < m)
    {
        if(s[i] == pat[j])
        {
            ++i;
            ++j;
        }
        else if(j == 0)
        {
            ++i;
        }
        else
        {
            j = nnext[j - 1];
        }
    }
    return (j == m) ? i - m : -1;
}
```

## 主函数

```cpp
int main()
{
    string s, pat;
    cin >> s >> pat;

    buildnnext(pat);

    for(int i = 0; i < (int)nnext.size(); ++i)
        cout << nnext[i] << " ";
    cout << endl;

    int pos = kmpSearch(s, pat);
    if(pos != -1)
        cout << "Pattern found at index: " << pos << endl;
    else
        cout << "Pattern not found." << endl;
    return 0;
}
```
