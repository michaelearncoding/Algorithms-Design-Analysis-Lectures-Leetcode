# 递归（recursive）是一种编程技术，指的是函数调用自身来解决问题。
# 递归通常用于解决可以被分解为更小的相同问题的场景。

# 理解递归的关键在于两个概念：
# 1. 基准条件（base case）：用于终止递归的条件，防止无限递归。
# 2. 递归条件（recursive case）：定义问题如何被分解为更小的子问题。


# 计算 n 的阶乘
def factorial(n):
    if n == 0:  # 基准条件
        return 1
    else:  # 递归条件
        return n * factorial(n - 1)

# 测试
print(factorial(5))  # 输出 120