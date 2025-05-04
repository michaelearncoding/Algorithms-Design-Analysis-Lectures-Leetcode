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
            fast = fast.next.next # 快指针每次走两步
            slow = slow.next # 慢指针每次走一步
            if fast == slow: # 如果快指针和慢指针相遇，说明链表中存在环
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


# 判断链表是否包含环属于经典问题了，解决方案也是用快慢指针：

# 每当慢指针 slow 前进一步，快指针 fast 就前进两步。

# 如果 fast 最终能正常走到链表末尾，说明链表中没有环；如果 fast 走着走着竟然和 slow 相遇了，那肯定是 fast 在链表中转圈了，说明链表中含有环。

# 只需要把寻找链表中点的代码稍加修改就行了：

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
            if slow == fast: # 假设没有重复出现的node/节点各自不相同
                return True
        # 不包含环
        return False