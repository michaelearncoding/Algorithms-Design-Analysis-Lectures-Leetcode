# 初始化左右指针：left = 0, right = len(arr) - 1
# 循环查找：每次取中间元素与目标比较
# 调整区间：根据比较结果缩小查找范围
# 返回结果：找到返回索引，未找到返回 -1

def binary_search(arr, target):
    """
    二分查找模板
    :param arr: 已排序的数组
    :param target: 要查找的目标值
    :return: 目标值的索引，如果不存在则返回 -1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2  # 防止溢出
        if arr[mid] == target:
            return mid  # 找到目标，返回索引
        elif arr[mid] < target:
            left = mid + 1  # 目标在右半部分
        else:
            right = mid - 1  # 目标在左半部分
    return -1  # 未找到目标

# 示例用法
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    index = binary_search(arr, target)
    print(f"Index of {target}: {index}")