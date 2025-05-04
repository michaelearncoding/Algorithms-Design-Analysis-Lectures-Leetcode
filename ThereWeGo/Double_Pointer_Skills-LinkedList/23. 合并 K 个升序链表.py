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
        # 优先级队列，最小堆
        pq = []
        # 将 k 个链表的头结点加入最小堆
        for i, head in enumerate(lists):
            if head is not None:
                heapq.heappush(pq, (head.val, i, head))

        while pq:
            # 获取最小节点，接到结果链表中
            val, i, node = heapq.heappop(pq)
            p.next = node
            if node.next is not None:
                heapq.heappush(pq, (node.next.val, i, node.next))
            # p 指针不断前进
            p = p.next
            
        return dummy.next
    

# template

def mergeKLists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left = mergeKLists(lists[:mid])
    right = mergeKLists(lists[mid:])
    return mergeTwoLists(left, right)

def mergeTwoLists(l1, l2):
    dummy = ListNode(-1)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next

