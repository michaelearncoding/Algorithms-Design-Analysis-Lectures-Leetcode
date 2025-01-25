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




class Solution:
    
    def __init__(self):
        self.res = []
        # 记录回溯算法的递归路径
        self.track = []

    # 主函数
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)
        return self.res
    
    # 回溯算法核心函数，遍历子集问题的回溯树
    def backtrack(self, nums: List[int], start: int) -> None:
        
        # 前序位置，每个节点的值都是一个子集
        self.res.append(list(self.track))
        
        # 回溯算法标准框架
        for i in range(start, len(nums)):
            # 做选择
            self.track.append(nums[i]) # 用 track 记录根节点到每个节点的路径的值
            # 通过 start 参数控制树枝的遍历，避免产生重复的子集
            self.backtrack(nums, i + 1)
            # 撤销选择
            self.track.pop()

