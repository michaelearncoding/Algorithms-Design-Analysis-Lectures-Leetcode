# https://leetcode.com/problems/merge-two-sorted-lists/description/
# 21. Merge Two Sorted Lists

# 双指针技巧秒杀七道链表题目
# https://labuladong.online/algo/essential-technique/linked-list-skills-summary-2/

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
            # 把最后剩下的节点接到 p 指针
            p.next = p1
        
        if p2 is not None:
            # 把最后剩下的节点接到 p 指针
            p.next = p2
        
        return dummy.next