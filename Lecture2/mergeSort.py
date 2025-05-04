def merge_sort(arr):
    """
    归并排序模板
    :param arr: 待排序数组
    :return: 排序后的新数组
    """
    # 基本情况：数组长度为1或0，直接返回
    if len(arr) <= 1:
        return arr

    # 1. 分治：将数组分为两半
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 2. 合并：将两个有序数组合并为一个有序数组
    return merge(left, right)

def merge(left, right):
    """
    合并两个有序数组
    """
    merged = []
    i = j = 0
    # 比较两个数组的元素，依次放入结果数组
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # 剩余元素直接加入
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# 示例用法
if __name__ == "__main__":
    arr = [5, 2, 4, 7, 1, 3, 2, 6]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)