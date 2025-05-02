# 核心思想：分治法（Divide & Conquer）：

# 分解：递归将数组分成两半，直到子数组长度为 1。

# 合并：将两个有序子数组合并成一个有序数组。

# logn for the depth of the recursion tree
# n for the merging process


# 标准实现（非原地排序）
def merge_sort(arr):

    if len(arr) <= 1: # 基准条件：当数组长度为 1 或 0 时，直接返回数组
        return arr
    
    mid = len(arr) // 2 # 递归条件# 找到数组的中点
    left = merge_sort(arr[:mid]) # 递归分解左半部分
    right = merge_sort(arr[mid:]) # 递归分解右半部分
    return merge(left, right) # 合并两个有序子数组

def merge(left, right):
    result = [] # 用于存储合并后的有序数组
    i = j = 0 # 两个指针分别指向 left 和 right 的起始位置
    while i < len(left) and j < len(right): # 比较两个数组的元素，按顺序将较小的元素加入 result
        if left[i] <= right[j]:
            result.append(left[i])  # 将 left[i] 加入 result
            i += 1 # 移动左数组的指针
        else:
            result.append(right[j])  # 将 right[j] 加入 result
            j += 1 # 移动右数组的指针
    # 将剩余的元素加入 result（如果有的话）
    result += left[i:]  # 将 left 中剩余的元素加入 result
    result += right[j:] # 将 right 中剩余的元素加入 result
    return result  # 返回合并后的有序数组



