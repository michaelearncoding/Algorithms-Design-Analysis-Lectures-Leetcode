# 伪码框架
def coinChange(coins: List[int], amount: int) -> int:
    # 题目要求的最终结果是 dp(amount)
    return dp(coins, amount)

# 定义：要凑出金额 n，至少要 dp(coins, n) 个硬币
def dp(coins: List[int], n: int) -> int:
    # 做选择，选择需要硬币最少的那个结果
    # 初始化res为正无穷
    res = float('inf')
    for coin in coins:
        res = min(res, sub_problem + 1)
    return res