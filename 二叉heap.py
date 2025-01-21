class MyPriorityQueue:
    # 在二叉堆堆顶插入一个元素，时间复杂度 O(logN)
    # N 为当前二叉堆中的元素个数
    def push(self, x: int):
        pass

    # 返回堆顶元素，时间复杂度 O(1)
    # 该堆顶元素就是二叉堆中的最大值或最小值，取决于是最大堆还是最小堆
    def peek(self) -> int:
        pass

    # 删除堆顶元素，时间复杂度 O(logN)
    def pop(self) -> int:
        pass

    # 返回堆中元素的个数，时间复杂度 O(1)
    def size(self) -> int:
        pass


# 另一种应用：堆排序
# 堆排序伪码，对 arr 原地排序
# 时间复杂度 O(NlogN)，空间复杂度 O(N)
def heapSort(arr):
    res = [0] * len(arr)
    pq = MyPriorityQueue()
    for x in arr:
        pq.push(x)
    # 元素出堆的顺序是有序的
    for i in range(len(arr)):
        res[i] = pq.pop()
    return res

