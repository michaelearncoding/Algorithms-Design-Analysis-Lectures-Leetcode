def min_heap_swim(heap, node):
    # 小顶堆的上浮操作，时间复杂度是树高 O(logN)
    while node > 0 and heap[parent(node)] > heap[node]: # 比较当前节点与其父节点的值。
        swap(heap, parent(node), node) # 如果当前节点的值大于父节点的值，则交换它们的位置。
        node = parent(node) 


def min_heap_sink(heap, node, size):
    # 小顶堆的下沉操作，时间复杂度是树高 O(logN)
    while left(node) < size or right(node) < size: # 比较当前节点与其左右子节点的值。
        # 比较自己和左右子节点，看看谁最小
        min_index = node
        # 如果当前节点的值小于最大的子节点的值，则交换它们的位置。
        if left(node) < size and heap[left(node)] < heap[min_index]:
            min_index = left(node)
        if right(node) < size and heap[right(node)] < heap[min_index]:
            min_index = right(node)
        if min_index == node:
            break
        # 如果左右子节点中有比自己小的，就交换
        swap(heap, node, min_index)
        node = min_index


def max_heap_swim(heap, node):
    # 大顶堆的上浮操作
    while node > 0 and heap[parent(node)] < heap[node]:
        swap(heap, parent(node), node)
        node = parent(node)


def max_heap_sink(heap, node, size):
    # 大顶堆的下沉操作
    while left(node) < size or right(node) < size:
        # 小顶堆和大顶堆的唯一区别就在这里，比较逻辑相反
        # 比较自己和左右子节点，看看谁最大
        max_index = node
        if left(node) < size and heap[left(node)] > heap[max_index]:
            max_index = left(node)
        if right(node) < size and heap[right(node)] > heap[max_index]:
            max_index = right(node)
        if max_index == node:
            break
        swap(heap, node, max_index)
        node = max_index


def parent(node):
    # 父节点的索引
    return (node - 1) // 2


def left(node):
    # 左子节点的索引
    return node * 2 + 1


def right(node):
    # 右子节点的索引
    return node * 2 + 2


def swap(heap, i, j):
    # 交换数组中两个元素的位置
    heap[i], heap[j] = heap[j], heap[i]


def sort(nums): 
    # 第一步，原地建堆，注意这里创建的是大顶堆
    # 只要从左往右对每个元素调用 swim 方法，就可以原地建堆
    for i in range(len(nums)):
        max_heap_swim(nums, i)

    # 第二步，排序
    # 现在整个数组已经是一个大顶了，直接模拟删除堆顶元素的过程即可
    heap_size = len(nums)
    while heap_size > 0:
        # 从堆顶删除元素，放到堆的后面
        swap(nums, 0, heap_size - 1)
        heap_size -= 1
        # 恢复堆的性质
        max_heap_sink(nums, 0, heap_size)
        # 现在 nums[0..heap_size) 是一个大顶堆，nums[heap_size..) 是有序元素

def sort(nums):
    # 第一步，原地建堆，注意这里创建的是大顶堆
    # 只要从左往右对每个元素调用 swim 方法，就可以原地建堆
    for i in range(len(nums)):
        max_heap_swim(nums, i)

    # 第二步，排序
    # 现在整个数组已经是一个大顶了，直接模拟删除堆顶元素的过程即可
    heap_size = len(nums)
    while heap_size > 0:
        # 从堆顶删除元素，放到堆的后面
        swap(nums, 0, heap_size - 1)
        heap_size -= 1
        # 恢复堆的性质
        max_heap_sink(nums, 0, heap_size)
        # 现在 nums[0..heap_size) 是一个大顶堆，nums[heap_size..) 是有序元素



