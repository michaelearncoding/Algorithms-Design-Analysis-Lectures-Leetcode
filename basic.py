# Playground
# single linked list node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# actuall programming
class Michael:
    def __init__(self, height, salary):
        self.height = height
        self.salary = salary
# it's a memory address


# framework for DFS - recusive traversal of a tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# binary tree traversal
def traveres(node: TreeNode): # the input value of the node is the instance of TreeNode
    if node is None:
        return
    traveres(node.left)
    traveres(node.right)


# framework for BFS - recusive traversal of a tree
from collections import deque

def levelOrderTraverse(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    while q:
        cur = q.popleft()
        # 访问 cur 节点
        print(cur.val)

        # 把 cur 的左右子节点加入队列
        if cur.left is not None:
            q.append(cur.left)
        if cur.right is not None:
            q.append(cur.right)