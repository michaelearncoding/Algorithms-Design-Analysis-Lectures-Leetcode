# # 力扣第 45 题「跳跃游戏 II」：

# 45. 跳跃游戏 II | 力扣 | LeetCode |  🟠
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

# 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

# 0 <= j <= nums[i] 
# i + j < n
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

# 示例 1:

# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 示例 2:

# 输入: nums = [2,3,0,1,4]
# 输出: 2
# 提示:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# 题目保证可以到达 nums[n-1]



class Solution:
    # 主函数
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # 备忘录都初始化为 n，相当于 INT_MAX
        # 因为从 0 跳到 n - 1 最多 n - 1 步
        memo = [n] * n

        return self.dp(nums, 0, memo)
    
    # 定义：从索引 p 跳到最后一格，至少需要 dp(nums, p) 步
    def dp(self, nums: List[int], p: int, memo: List[int]) -> int:
        n = len(nums)
        # base case
        if p >= n - 1:
            return 0
        # 子问题已经计算过
        if memo[p] != n:
            return memo[p]
        steps = nums[p] # 这里就是题目的定义
        # 你可以选择跳 1 步，2 步...
        for i in range(1, steps + 1): # 这里就是说根据上面的值，你不一定要跳那么多，你可以从1开始，最多不超过steps+1
            # 穷举每一个选择
            # 计算每一个子问题的结果
            subProblem = self.dp(nums, p + i, memo)
            # 取其中最小的作为最终结果
            memo[p] = min(memo[p], subProblem + 1)
        return memo[p]