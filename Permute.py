class Solution:
    def __init__(self):
        # 存储所有排列结果的列表
        self.res = []
        # 记录回溯算法的递归路径
        self.track = []
        # track 中的元素会被标记为 true
        self.used = []
    
    # 主函数，输入一组不重复的数字，返回它们的全排列
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.used = [False] * len(nums)
        self.backtrack(nums)
        return self.res
    
    # 回溯算法核心函数
    def backtrack(self, nums: List[int]) -> None:
        # base case，到达叶子节点
        if len(self.track) == len(nums):
            # 收集叶子节点上的值
            self.res.append(self.track[:])
            return
        
        # 回溯算法标准框架
        for i in range(len(nums)):
            # 已经存在 track 中的元素，不能重复选择
            if self.used[i]:
                continue
            # 做选择
            self.used[i] = True
            self.track.append(nums[i])
            # 进入下一层回溯树
            self.backtrack(nums)
            # 取消选择
            self.track.pop()
            self.used[i] = False

