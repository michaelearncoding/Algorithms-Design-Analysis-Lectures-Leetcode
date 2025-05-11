import bisect

right = [3, 4, 7, 8]  # 右半边已经排好序
x = 6                 # 左半边的某个元素

# bisect_left 返回第一个 >= x 的下标
count = bisect.bisect_left(right, x)
print(count)  # 输出2，说明有2个元素（3,4）小于6



# 只需要take care第三种情况，就是跨越左右两边的index 对 
# 二分查找只用于左半边的每个元素，去右半边（已排序）查找比它小的元素个数。

# 二分查找
# 时间复杂度O(logn)
# 用于查找，计数或者插入等场景
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # 找到目标，返回下标
        elif arr[mid] < target:
            left = mid + 1  # 去右半边找
        else:
            right = mid - 1  # 去左半边找
    return -1  # 没找到

# 查找第一个大于等于 target 的位置（lower_bound）
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left  # 返回第一个 >= target 的下标
# 如果你想找有多少个元素小于 target，直接返回 left 就是答案。

# 查找第一个大于 target 的位置（upper_bound）
def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left  # 返回第一个 > target 的下标


import bisect

arr = [1, 3, 4, 6, 8]
x = 5
print(bisect.bisect_left(arr, x))  # 输出 3，表示有3个元素 < 5
print(bisect.bisect_right(arr, x)) # 输出 3，表示有3个元素 <= 5

# 排序的算法


'''

merge_sort([5, 2, 4, 1])
  ├─ merge_sort([5, 2])
  │    ├─ merge_sort([5])   ← 入栈
  │    └─ merge_sort([2])   ← 入栈
  │    ← 合并 [5], [2]      ← 出栈
  └─ merge_sort([4, 1])
       ├─ merge_sort([4])   ← 入栈
       └─ merge_sort([1])   ← 入栈
       ← 合并 [4], [1]      ← 出栈
  ← 合并 [2, 5], [1, 4]     ← 出栈

'''

# 入栈：递归分解问题，直到最小子问题。
# 出栈：递归回溯，合并子问题的解，逐步返回上一层。
# 归并排序的递归过程就是不断“入栈-出栈”，直到排序完成。


for x in left:  # left 是左半边，已经排好序
    count += bisect.bisect_left(right, x)  # right 是右半边，已排序




def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



# https://www.youtube.com/watch?v=xli_FI7CuzA
# 2分钟冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 每一轮把最大的元素“冒泡”到最后
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换相邻元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 示例
arr = [5, 2, 4, 1, 3]
bubble_sort(arr)
print(arr)  # 输出: [1, 2, 3, 4, 5]


