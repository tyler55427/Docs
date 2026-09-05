# BM

**问题描述**：在文本串 s 中查找模式串 pat 的首次出现位置。

**解法**：BM 算法，采用坏字符规则和好后缀规则，从模式串尾部向前匹配，失配时根据两条规则选择最大位移。时间复杂度最坏 O(n·m)，实际应用中通常比 KMP 更快。

## 全局变量

```cpp
string s;          // 文本串
string pat;        // 模式串
vector<int> bad;   // 坏字符规则表
vector<int> good;  // 好后缀规则表
vector<int> nxt;   // 辅助数组（类似 KMP 的 next）
```

## 构建坏字符规则表

bad[c] = 模式串中字符 c 最后出现位置到末尾的距离。失配时，将模式串中"最后一个"该字符与当前文本位置对齐。

```cpp
void buildBadCharRule()
{
    int m = pat.length();
    bad.assign(256, m);
    for(int i = 0; i < m; ++i)
    {
        bad[(unsigned char)pat[i]] = m - 1 - i;
    }
}
```

## 构建好后缀规则表

good[i] = 模式串中位置 i 之前的后缀，与模式串某前缀匹配时的位移。处理三种情况：后缀完全在前缀中、后缀的部分子集在前缀中、后缀的子串在前缀的字串中（不包括开头）。

```cpp
void buildGoodSuffixRule()
{
    int m = pat.length();
    good.assign(m, 0);
    nxt.assign(m, 0);

    int i = 0, j = 1;
    while(j < m)
    {
        if(pat[i] == pat[j])
        {
            nxt[j] = i + 1;
            ++i;
            ++j;
        }
        else if(i == 0)
        {
            ++j;
        }
        else
        {
            i = nxt[i - 1];
        }
    }

    int lastpos = m - 1;
    for(int i = 0; i < m; ++i)
    {
        good[i] = lastpos * 2 - i;
    }

    int pos = lastpos;
    int last_i = lastpos;
    while(nxt[pos] > 0)
    {
        int start, end;
        if(pos == lastpos) start = 0;
        else start = m - nxt[last_i];

        end = m - nxt[last_i];
        for(int j = start; j < end; ++j)
            good[j] = lastpos * 2 - j - nxt[pos];

        last_i = pos;
        pos = nxt[pos] - 1;
    }

    int j = lastpos;
    int t = m;
    while(true)
    {
        nxt[j] = t;
        while(t < m && pat[j] != pat[t])
        {
            good[t] = min(good[t], lastpos - 1 - j);
            t = nxt[t];
        }
        --t;
        if(j == 0) break;
        --j;
    }
    good[lastpos] = 0;
}
```

## 匹配规则

坏字符规则和好后缀规则的位移计算函数。

```cpp
int delta1(char c)
{
    return bad[(unsigned char)c];
}

int delta2(int j)
{
    return good[j];
}
```

## BM 匹配函数

从模式串末尾向前匹配，失配时根据坏字符和好后缀规则选择最大位移。

```cpp
int bmSearch()
{
    int n = s.length();
    int m = pat.length();

    int i = m - 1;
    int j = m - 1;

    while(true)
    {
        if(j < 0) return i + 1;

        if(s[i] == pat[j])
        {
            --i;
            --j;
            continue;
        }

        int d1 = delta1(s[i]);
        int d2 = delta2(j);
        i += max(d1, d2);

        if(i >= n) return -1;

        j = m - 1;
    }
}
```

## 主函数

```cpp
int main()
{
    cin >> s >> pat;

    buildBadCharRule();
    buildGoodSuffixRule();

    int pos = bmSearch();
    if(pos != -1)
        cout << "Pattern found at index: " << pos << endl;
    else
        cout << "Pattern not found." << endl;
    return 0;
}
```
