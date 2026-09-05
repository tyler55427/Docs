# 第k个最大元素

## 第k个最大元素

**问题描述**：给定一个整数数组和一个整数 k，找出数组中第 k 个最大的元素。

**解法**：使用一个最小堆来维护当前最大的 k 个元素

**备注**：对应第 n-k 小，重复删除 n-k 的最小

```cpp
int findKthLargest(vector<int>& nums, int k) {
    // 小根堆
    priority_queue<int, vector<int>, greater<int>> heap;
    
    for (int num : nums) {
        heap.push(num);
        if (heap.size() > k) {
            heap.pop();
        }
    }
    
    return heap.top();
}
```
