def bfs(graph, s):
    visited = [False] * len(graph)  # 初始化一个列表，记录每个节点是否被访问过
    q = deque([s])  # 使用双端队列来存储待访问的节点，初始时包含起始节点 s
    visited[s] = True  # 标记起始节点 s 为已访问
    step = 0  # 记录从起始节点 s 到当前节点的步数
    
    while q:  # 当队列不为空时，继续遍历
        sz = len(q)  # 当前队列中的节点数
        for i in range(sz):  # 遍历当前层的所有节点
            cur = q.popleft()  # 从队列中取出一个节点
            print(f"visit {cur} at step {step}")  # 打印当前访问的节点和步数
            if cur == target:  # 判断是否到达目标节点
                return step  # 如果到达目标节点，返回步数

            for to in neighborsOf(cur):  # 遍历当前节点的所有邻居节点
                if not visited[to]:  # 如果邻居节点未被访问
                    q.append(to)  # 将邻居节点加入队列
                    visited[to] = True  # 标记邻居节点为已访问
        step += 1  # 每遍历完一层，步数加一
    
    return -1  # 如果遍历完所有节点仍未找到目标节点，返回 -1

# 记录一维字符串的相邻索引
neighbor = [
    [1, 3],
    [0, 4, 2],
    [1, 5],
    [0, 4],
    [3, 1, 5],
    [4, 2]
]


# 滑动谜题：

from collections import deque

class Solution:
    def slidingPuzzle(self, board):
        target = "123450"
        # 将 2x3 的数组转化成字符串作为 BFS 的起点
        start = ""
        for i in range(len(board)):
            for j in range(len(board[0])):
                start += str(board[i][j])
        
        # ****** BFS 算法框架开始 ******
        q = deque()
        visited = set()
        # 从起点开始 BFS 搜索
        q.append(start)
        visited.add(start)
        
        step = 0
        while q: 
            # 当前层的节点数量
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                # 判断是否达到目标局面
                if cur == target:
                    return step
                # 将数字 0 和相邻的数字交换位置
                for neighbor_board in self.getNeighbors(cur):
                    # 防止走回头路
                    if neighbor_board not in visited:
                        q.append(neighbor_board)
                        visited.add(neighbor_board)
            step += 1
        # ****** BFS 算法框架结束 ******
        return -1

    def getNeighbors(self, board):
        # 记录一维字符串的相邻索引
        mapping = [
            [1, 3],
            [0, 4, 2],
            [1, 5],
            [0, 4],
            [3, 1, 5],
            [4, 2]
        ] 
        
        idx = board.index('0')
        neighbors = []
        for adj in mapping[idx]:
            new_board = self.swap(board, idx, adj)
            neighbors.append(new_board)
        return neighbors

    def swap(self, board, i, j):
        chars = list(board)
        chars[i], chars[j] = chars[j], chars[i]
        return ''.join(chars)






# 二叉树计算答案的思路：遍历一遍二叉树，用一个外部变量记录每个节点所在的深度，取最大值就可以得到最大深度
class Solution:
    def __init__(self):
        # 记录最大深度
        self.res = 0
        # 记录遍历到的节点的深度
        self.depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.res

    # 二叉树遍历框架
    def traverse(self, root: TreeNode) -> None:
        if root is None:
            return
        # 前序位置
        self.depth += 1
        if root.left is None and root.right is None:
            # 到达叶子节点，更新最大深度
            self.res = max(self.res, self.depth)
        self.traverse(root.left)
        self.traverse(root.right)
        # 后序位置
        self.depth -= 1


class Solution:
    # 定义：输入根节点，返回这棵二叉树的最大深度
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # 利用定义，计算左右子树的最大深度
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        # 整棵树的最大深度等于左右子树的最大深度取最大值，
        # 然后再加上根节点自己
        res = max(leftMax, rightMax) + 1

        return res


# 分解问题的思路：将问题分解成一个个子问题，然后递归求解子问题
class Solution:
    # 定义：输入一棵二叉树的根节点，返回这棵树的前序遍历结果
    def preorderTraversal(self, root):
        res = []
        if root == None:
            return res
        # 前序遍历的结果，root.val 在第一个
        res.append(root.val)
        # 利用函数定义，后面接着左子树的前序遍历结果
        res.extend(self.preorderTraversal(root.left))
        # 利用函数定义，最后接着右子树的前序遍历结果
        res.extend(self.preorderTraversal(root.right)) 
        return res