def traverse(root):
    if root is None:
        return
    # 遍历过的每个节点的值加一
    root.val += 1
    traverse(root.left)
    traverse(root.right)

# 你看，这就是 DFS 算法遍历的思路，它的着眼点永远是在单一的节点上，类比到二叉树上就是处理每个「节点」。

# 你再看看具体的 DFS 算法问题，比如 
# 一文秒杀所有岛屿题目 中讲的前几道题，我们的关注点是 grid 数组的每个格子（节点），我们要对遍历过的格子进行一些处理，所以我说是用 DFS 算法解决这几道题的：



# 对比 dfs 和 回溯法
# DFS 算法把「做选择」「撤销选择」的逻辑放在 for 循环外面
def dfs(root):
    if root is None:
        return
    # 做选择
    print("enter node %s" % root)
    for child in root.children:
        dfs(child)
    # 撤销选择
    print("leave node %s" % root)

# 回溯算法把「做选择」「撤销选择」的逻辑放在 for 循环里面
def backtrack(root):
    if root is None:
        return
    for child in root.children:
        # 做选择
        print("I'm on the branch from %s to %s" % (root, child))
        backtrack(child)
        # 撤销选择
        print("I'll leave the branch from %s to %s" % (child, root))