def binary_search_recursive(arr, target, left, right):
    if left > right: # 基准条件：如果左边界超过右边界，说明目标值不存在
        return -1 
    mid = (left + right) // 2 # 找到当前搜索范围的中间索引
    if arr[mid] == target: # 如果中间值等于目标值
        return mid # 找到目标值，返回其索引
    elif arr[mid] < target: # 如果中间值小于目标值
        return binary_search_recursive(arr, target, mid + 1, right)
    else: # 如果中间值大于目标值
        return binary_search_recursive(arr, target, left, mid - 1)