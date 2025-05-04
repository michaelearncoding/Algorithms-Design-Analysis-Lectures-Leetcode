# 单链表的中点

class Solution:
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


# template
