# 如何遍历 + 访问？我们仍然从最高层来看，各种数据结构的遍历 + 访问无非两种形式：线性的和非线性的。

#线性就是 for/while 迭代为代表，非线性就是递归为代表。再具体一步，无非以下几种框架：

# classic linear iteration template

# def traverse(arr: List[int]):
#     for i in range(len(arr)):
#         # 迭代访问 arr[i]

# 链表遍历框架，兼具迭代和递归结构：

# 基本的单链表节点
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def traverse(head: ListNode) -> None:
    p = head
    while p is not None:
        # 迭代访问 p.val
        p = p.next

def traverse(head: ListNode) -> None:
    # 递归访问 head.val
    traverse(head.next)

# 二叉树遍历框架，典型的非线性递归遍历结构：
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def traverse(root: TreeNode):
    traverse(root.left)
    traverse(root.right)

# N gram tree can also extented to the graph traversal
# 基本的 N 叉树节点
class TreeNode:
    val: int
    children: List[TreeNode]

def traverse(root: TreeNode) -> None:
    for child in root.children:
        traverse(child)
