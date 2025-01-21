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




