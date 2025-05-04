# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 示例 2：

# 输入：l1 = [], l2 = []
# 输出：[]
# 示例 3：

# 输入：l1 = [], l2 = [0]
# 输出：[0]


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
    

# template : 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    """
    合并两个有序链表，返回新链表的头节点
    :param l1: ListNode，链表1的头节点
    :param l2: ListNode，链表2的头节点
    :return: ListNode，合并后链表的头节点
    """
    dummy = ListNode(-1)  # 哨兵节点，简化操作
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # 处理剩余部分
    current.next = l1 if l1 else l2

    return dummy.next