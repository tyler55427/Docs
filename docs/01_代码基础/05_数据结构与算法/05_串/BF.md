# BF

**问题描述**：在文本串 s 中查找模式串 pat 的**首次**出现位置。

**解法**：

- 暴力匹配。
- 逐个字符比较，失配时模式串右移一位，文本串指针回退。
- 时间复杂度最坏 O(n·m)。

```cpp
int bruteForceSearch(const string& s, const string& pat)
{
    int n = s.length();
    int m = pat.length();

    if(m > n) return -1;

    for(int i = 0; i <= n - m; ++i)
    {
        int j = 0;
        while(j < m && s[i + j] == pat[j])
        {
            ++j;
        }
        if(j == m)
        {
            return i;
        }
    }
    return -1;
}
```

**问题描述**：在文本串 s 中查找模式串 pat 的**所有**出现位置。

**解法**：从文本串每个位置依次匹配，收集所有匹配成功的起始位置。

```cpp
vector<int> bruteForceSearchAll(const string& s, const string& pat)
{
    vector<int> result;
    int n = s.length();
    int m = pat.length();

    if(m > n) return result;

    for(int i = 0; i <= n - m; ++i)
    {
        int j = 0;
        while(j < m && s[i + j] == pat[j])
        {
            ++j;
        }
        if(j == m)
        {
            result.push_back(i);
        }
    }
    return result;
}
```
