# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
# 示例 2：

# 输入：head = [2,1], x = 2
# 输出：[1,2]

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

# template

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    """
    分隔链表模板
    :param head: ListNode，链表头节点
    :param x: int，分隔值
    :return: ListNode，分隔后链表的头节点
    """
    # 虚拟头结点，分别用于小于x和大于等于x的链表
    dummy1 = ListNode(-1)
    dummy2 = ListNode(-1)
    p1, p2 = dummy1, dummy2
    p = head

    while p:
        if p.val < x:
            p1.next = p
            p1 = p1.next
        else:
            p2.next = p
            p2 = p2.next
        # 断开原链表，防止成环
        temp = p.next
        p.next = None
        p = temp

    # 连接两个链表
    p1.next = dummy2.next
    return dummy1.next

