# 核心思想：分治法（Divide & Conquer）：

# 分解：递归将数组分成两半，直到子数组长度为 1。

# 合并：将两个有序子数组合并成一个有序数组。

# logn for the depth of the recursion tree
# n for the merging process


# 标准实现（非原地排序）
def merge_sort(arr):

    if len(arr) <= 1: # 基准条件
        return arr
    
    mid = len(arr) // 2 # 递归条件
    left = merge_sort(arr[:mid]) # 分解
    right = merge_sort(arr[mid:]) # 分解
    return merge(left, right) # 合并

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
    result += left[i:]
    result += right[j:]
    return result