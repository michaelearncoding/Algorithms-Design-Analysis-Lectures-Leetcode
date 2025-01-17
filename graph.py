# 图节点的逻辑结构
class Vertex:
    def __init__(self, id: int):
        self.id = id
        self.neighbors = []


# 基本的 N 叉树节点
class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []