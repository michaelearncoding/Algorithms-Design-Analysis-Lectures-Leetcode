# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Ref: 
# 链表: 1->2->3->4->5，删除倒数第2个节点(节点4)
# 创建虚拟头节点
# dummy -> 1 -> 2 -> 3 -> 4 -> 5
# return dummy.next  # 返回1->2->3->5
# 这个算法巧妙之处在于使用两个指针的间距来定位倒数第N个节点，只需遍历一次链表。


# 返回链表的倒数第 k 个节点
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
    # p2 现在指向第 n - k + 1 个节点，即倒数第 k 个节点
    return p2


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
        
    def findFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 代码见上文
        pass