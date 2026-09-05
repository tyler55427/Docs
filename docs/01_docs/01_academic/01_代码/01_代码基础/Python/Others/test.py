import random

array = [69, 79, 75, 4, 47, 18, 18, 55, 31, 68, 61, 40, 95, 63, 4, 76, 75, 42, 94, 77]

# for i in range(random.randint(10, 100)):
#     array.append(random.randint(0, 100))
    
k = 2

# print("生成的随机数组为：", array, k, i)

# 使用双端队列完成滑动窗口的最大值问题
from collections import deque
def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []
    
    deq = deque()
    max_values = []
    
    for i in range(len(nums)):
        # Remove indices that are out of the current window
        if deq and deq[0] < i - k + 1:
            deq.popleft()
        
        # Remove elements from the deque that are less than the current element
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        
        # Add the current index to the deque
        deq.append(i)
        
        # If we have filled at least k elements, add the maximum to the result
        if i >= k - 1:
            max_values.append(nums[deq[0]])
    
    return max_values

# Test the function
result = max_sliding_window(array, k)
print("使用双端队列的滑动窗口最大值为：", result)

ans = []
for i in range(len(array)):
    if i < k:
        while ans and ans[-1][1] < array[i]:
            ans.pop()
        ans.append((i, array[i]))
    else:
        while ans[0][0] <= i - k:
            ans.remove(ans[0])
        
        while ans and ans[-1][1] < array[i]:
            ans.pop()
        ans.append((i, array[i]))
        
    if i >= k - 1:
        print("滑动窗口最大值为：", ans[0][1]==result[i - k + 1])
            