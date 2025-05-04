class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # p1 指向 A 链表头结点，p2 指向 B 链表头结点
        p1, p2 = headA, headB
        while p1 != p2:
            # p1 走一步，如果走到 A 链表末尾，转到 B 链表
            p1 = p1.next if p1 else headB
            # p2 走一步，如果走到 B 链表末尾，转到 A 链表
            p2 = p2.next if p2 else headA
        return p1

#说实话我没有想到这种思路，不得不说这是一个很巧妙的转换！不过需要注意的是，这道题说不让你改变原始链表的结构，所以你把题目输入的链表转化成环形链表求解之后记得还要改回来，否则无法通过。

# 另外，还有读者提到，既然「寻找两条链表的交点」的核心在于让 p1 和 p2 两个指针能够同时到达相交节点 c1，那么可以通过预先计算两条链表的长度来做到这一点，具体代码如下：

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        # 计算两条链表的长度
        p1, p2 = headA, headB
        while p1:
            lenA += 1
            p1 = p1.next
        while p2:
            lenB += 1
            p2 = p2.next
        
        # 让 p1 和 p2 到达尾部的距离相同
        p1, p2 = headA, headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                p1 = p1.next
        else:
            for _ in range(lenB - lenA):
                p2 = p2.next
        
        # 看两个指针是否会相同，p1 == p2 时有两种情况：
        # 1、要么是两条链表不相交，他俩同时走到尾部空指针
        # 2、要么是两条链表相交，他俩走到两条链表的相交点
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # p1 指向 A 链表头结点，p2 指向 B 链表头结点
        p1, p2 = headA, headB
        while p1 != p2:
            # p1 走一步，如果走到 A 链表末尾，转到 B 链表
            p1 = p1.next if p1 else headB
            # p2 走一步，如果走到 B 链表末尾，转到 A 链表
            p2 = p2.next if p2 else headA
        return p1

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        # 计算两条链表的长度
        p1, p2 = headA, headB
        while p1:
            lenA += 1
            p1 = p1.next
        while p2:
            lenB += 1
            p2 = p2.next
        
        # 让 p1 和 p2 到达尾部的距离相同
        p1, p2 = headA, headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                p1 = p1.next
        else:
            for _ in range(lenB - lenA):
                p2 = p2.next
        
        # 看两个指针是否会相同，p1 == p2 时有两种情况：
        # 1、要么是两条链表不相交，他俩同时走到尾部空指针
        # 2、要么是两条链表相交，他俩走到两条链表的相交点
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
