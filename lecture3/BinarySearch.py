import bisect

right = [3, 4, 7, 8]  # 右半边已经排好序
x = 6                 # 左半边的某个元素

# bisect_left 返回第一个 >= x 的下标
count = bisect.bisect_left(right, x)
print(count)  # 输出2，说明有2个元素（3,4）小于6



# 只需要take care第三种情况，就是跨越左右两边的index 对 
# 二分查找只用于左半边的每个元素，去右半边（已排序）查找比它小的元素个数。


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

