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


#这里先直接看一下寻找环起点的解法代码：

class Solution:
    def detectCycle(self, head: ListNode):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        # 上面的代码类似 hasCycle 函数
        if not fast or not fast.next:
            # fast 遇到空指针说明没有环
            return None
        
        # 重新指向头结点
        slow = head 
        # 快慢指针同步前进，相交点就是环起点
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow

