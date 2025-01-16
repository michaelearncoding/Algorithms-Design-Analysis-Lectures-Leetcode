# single lINKED LIST
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 输入一个数组，转换为一条单链表
def createLinkedList(arr: 'List[int]') -> 'ListNode':
    if arr is None or len(arr) == 0:
        return None

    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next

    return head


# 创建链表的头节点，并通过循环依次创建链表的其余节点，最后返回链表的头节点。


# 创建一条单链表
head = createLinkedList([1, 2, 3, 4, 5])

# 在第 3 个节点后面插入一个新节点 66
# 先要找到前驱节点，即第 3 个节点
p = head
for _ in range(2):
    p = p.next
# 此时 p 指向第 3 个节点
# 组装新节点的后驱指针
new_node = ListNode(66)
new_node.next = p.next

# 插入新节点
p.next = new_node

# 现在链表变成了 1 -> 2 -> 3 -> 66 -> 4 -> 5