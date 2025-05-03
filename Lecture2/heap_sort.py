def heapify(arr, n, i):
    """
    将以索引 i 为根的子树调整为最大堆。
    :param arr: 待排序数组
    :param n: 数组的长度
    :param i: 当前需要调整的节点索引
    """
    largest = i  # 假设当前节点是最大值
    left = 2 * i + 1  # 左子节点索引
    right = 2 * i + 2  # 右子节点索引

    # 如果左子节点存在且大于当前最大值
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右子节点存在且大于当前最大值
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大值不是当前节点，则交换，并递归调整
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)  # 递归调整子树

def heap_sort(arr):
    """
    堆排序主函数。
    :param arr: 待排序数组
    """
    n = len(arr)

    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):  # 从最后一个非叶子节点开始
        heapify(arr, n, i)

    # 逐步将堆顶元素（最大值）移到数组末尾，并调整堆
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # 将堆顶元素与末尾元素交换
        heapify(arr, i, 0)  # 调整剩余的堆

# 测试代码
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    print("原始数组:", arr)
    heap_sort(arr)
    print("排序后数组:", arr)