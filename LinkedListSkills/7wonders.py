# 合并两个有序链表
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 虚拟头结点
        dummy = ListNode(-1)
        p = dummy
        p1 = l1
        p2 = l2
        
        while p1 is not None and p2 is not None: 
            # 比较 p1 和 p2 两个指针
            # 将值较小的的节点接到 p 指针
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            # p 指针不断前进
            p = p.next
        
        if p1 is not None:
            p.next = p1
        
        if p2 is not None:
            p.next = p2
        
        return dummy.next
    
# l1, l2 类似于拉链两侧的锯齿，指针 p 就好像拉链的拉索，将两个有序链表合并。

# 单链表的分解
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        # 存放小于 x 的链表的虚拟头结点
        dummy1 = ListNode(-1)
        # 存放大于等于 x 的链表的虚拟头结点
        dummy2 = ListNode(-1)
        # p1, p2 指针负责生成结果链表
        p1, p2 = dummy1, dummy2

        # p 负责遍历原链表，类似合并两个有序链表的逻辑
        # 这里是将一个链表分解成两个链表
        p = head
        while p:
            if p.val >= x:
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next
            # 不能直接让 p 指针前进，
            # p = p.next
            # 断开原链表中的每个节点的 next 指针
            temp = p.next
            p.next = None
            p = temp
        # 连接两个链表
        p1.next = dummy2.next

        return dummy1.next


# 合并 k 个有序链表, 因此有k个各自的最小节点
# similar to heap!!!! swim & sink methods 

def min_heap_swim(heap, node):
    # 小顶堆的上浮操作，时间复杂度是树高 O(logN)
    while node > 0 and heap[parent(node)] > heap[node]:
        swap(heap, parent(node), node)
        node = parent(node)

def min_heap_sink(heap, node, size):
    # 小顶堆的下沉操作，时间复杂度是树高 O(logN)
    while left(node) < size or right(node) < size:
        # 比较自己和左右子节点，看看谁最小
        min_index = node
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

# 具体实现

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # 重载比较运算符，方便将 ListNode 加入最小堆
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        # 虚拟头结点
        dummy = ListNode(-1)
        p = dummy

        # 优先级队列，最小堆 -> 初始化最小堆:
        pq = []
        # 将 k 个链表的头结点加入最小堆
        for i, head in enumerate(lists):
            if head is not None:
                heapq.heappush(pq, (head.val, i, head))

        while pq:
            # 获取最小节点，接到结果链表中 -》 从最小堆中取出最小的节点，将其加入结果链表。
            val, i, node = heapq.heappop(pq)
            p.next = node
            if node.next is not None: # 如果取出的节点有下一个节点，将下一个节点加入最小堆。
                heapq.heappush(pq, (node.next.val, i, node.next)) # 将节点的下一个节点加入堆中。
            # p 指针不断前进
            p = p.next
            
        return dummy.next

# 链表1: 1 -> 4 -> 5
# 链表2: 1 -> 3 -> 4
# 链表3: 2 -> 6

lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]

solution = Solution()
merged_list = solution.mergeKLists(lists)

# 打印合并后的链表
current = merged_list
while current:
    print(current.val, end=" -> ")
    current = current.next




# 单链表的倒数第k个节点

def findFromEnd(head: ListNode, k: int) -> ListNode:
    p1 = head
    # p1 先走 k 步
    for i in range(k):
        p1 = p1.next
    p2 = head
    # p1 和 p2 同时走 n - k 步
    while p1 != None:
        p2 = p2.next
        p1 = p1.next
    # 若p1 走到了尾节点，p2 正好走到了倒数第 k 个节点
    # 时间复杂度: 这种方法只需要遍历链表一次，时间复杂度是 (O(n))，其中 (n) 是链表的长度。
    # p2 现在指向第 n - k + 1 个节点，即倒数第 k 个节点
    return p2


# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# 主函数
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 虚拟头结点
        dummy = ListNode(-1)
        dummy.next = head
        # 删除倒数第 n 个，要先找倒数第 n + 1 个节点
        x = self.findFromEnd(dummy, n + 1)

        # 删掉倒数第 n 个节点
        x.next = x.next.next
        return dummy.next
    

# Middle of the Linked List
# 单链表的中点

class Solution: # 快慢指针
    def middleNode(self, head: ListNode) -> ListNode:
        # 快慢指针初始化指向 head
        slow, fast = head, head
        # 快指针走到末尾时停止
        while fast is not None and fast.next is not None:
            # 慢指针走一步，快指针走两步
            slow = slow.next
            fast = fast.next.next
        # 慢指针指向中点
        return slow
# 需要注意的是，如果链表长度为偶数，也就是说中点有两个的时候，我们这个解法返回的节点是靠后的那个节点。

# 判断链表是否包含环
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 快慢指针初始化指向 head
        slow, fast = head, head
        # 快指针走到末尾时停止
        while fast is not None and fast.next is not None:
            # 慢指针走一步，快指针走两步
            slow = slow.next
            fast = fast.next.next
            # 快慢指针相遇，说明含有环
            if slow == fast:
                return True
        # 不包含环
        return False


# 寻找环起点
# 背后有数学原理！
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if not fast or not fast.next:
            return None
        
        slow = head 

        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow
    


# 两个链表是否相交

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # p1 指向 A 链表头结点，p2 指向 B 链表头结点
        p1, p2 = headA, headB
        while p1 != p2:
            # p1 走一步，如果走到 A 链表末尾，转到 B 链表
            p1 = p1.next if p1 else headB
            # p2 走一步，如果走到 B 链表末尾，转到 A 链表
            p2 = p2.next if p2 else headA
        return p1



