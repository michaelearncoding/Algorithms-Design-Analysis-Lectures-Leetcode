# 二叉树题型主要是用来培养递归思维的，而层序遍历属于迭代遍历，也比较简单，这里就过一下代码框架吧：
# 1. 初始化一个队列，将根节点放入队列

# 输入一棵二叉树的根节点，层序遍历这棵二叉树
def levelTraverse(root: TreeNode) -> None:
    if root is None:
        return
    q = [root]

    # 从上到下遍历二叉树的每一层
    while q:
        sz = len(q)
        # 从左到右遍历每一层的每个节点
        for _ in range(sz):
            cur = q.pop(0)
            # 将下一层节点放入队列
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)