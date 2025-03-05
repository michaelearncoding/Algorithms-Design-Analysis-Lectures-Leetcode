# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Ref: 

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