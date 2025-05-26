
'''
1. 字符串处理

题目示例
反转字符串
判断回文
字符串中第一个不重复字符
字符串查找与替换


'''

# 反转字符串
def reverse_string(s):
    return s[::-1]

# 判断回文
def is_palindrome(s):
    return s == s[::-1]

# 第一个不重复字符
def first_unique_char(s):
    from collections import Counter
    count = Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1


'''

2. 数组/链表操作

题目示例
数组去重
合并两个有序数组/链表
寻找数组中的最大/最小值
移动零


'''

#  数组去重（原地）
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


# 合并两个有序链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


'''
3. 哈希表/集合应用

题目示例
两数之和
判断是否有重复元素
找出数组中只出现一次的数字

'''

# 两数之和
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i

# 判断是否有重复元素
def contains_duplicate(nums):
    return len(nums) != len(set(nums))


'''

4. 栈与队列
题目示例
有效的括号
用栈实现队列/用队列实现栈
最小栈

'''
# 有效的括号
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:  # 如果是右括号
            top = stack.pop() if stack else '#'  # 弹出栈顶元素
            if mapping[char] != top:  # 检查是否匹配
                return False
        else:
            stack.append(char)  # 左括号入栈
    return not stack  # 栈为空则有效


# 详细解释
# stack 用来存放左括号。
# mapping 是一个字典，记录每个右括号对应的左括号。
# 遍历字符串：
# 如果遇到右括号（如 )），就弹出栈顶元素，看是否和 ( 匹配。
# 如果遇到左括号（如 (），就直接入栈。
# 最后如果栈为空，说明所有括号都能正确配对。


'''
5. 简单递归与回溯
题目示例
斐波那契数列
全排列
子集


'''

# 斐波那契数列（递归+记忆化）

def fib(n, memo={}):
    # 优化：加上记忆化，避免重复计算。
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# 全排列
def permute(nums):

    res = []

    def backtrack(path, used):

        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):

            if used[i]:
                continue
                # 这意味着只是不处理已经用过的元素，而不是结束整个 for 循环。
                
            used[i] = True
            path.append(nums[i]) # 选择当前元素
            backtrack(path, used) # 递归，继续选择下一个

            path.pop() # 撤销选择，回到上一步
            used[i] = False

    backtrack([], [False]*len(nums))
    return res

# 子集
'''

总结口诀
range(start, ...) 保证只往后选，防止重复。
append + backtrack + pop 保证每条路径都被遍历，防止遗漏。
每次递归都记录当前 path，保证所有子集都被收集。


'''
# 核心思想：
# 每个元素都有两种选择：要或者不要。
# 我们可以用回溯（递归）的方法，枚举所有可能的选择。

'''

                []
              /    \
           [1]     []
          /   \       /    \
      [1,2]  [1]     [2]   []
      / \    /    \   / \
[1,2,3][1,2] [1,3][1] [2,3][2] [3][]

'''


def subsets(nums):
    res = []

    def backtrack(start, path):

        res.append(path[:]) # 收集当前子集

        for i in range(start, len(nums)):
            path.append(nums[i])  # 选择当前元素
            backtrack(i+1, path) # 递归，继续选择下一个
            path.pop() # 撤销选择，回到上一步

    backtrack(0, [])
    return res

'''
4. 直观理解
每个元素都可以选或不选，所以有 2^n个子集。
回溯法就是“试探”所有可能的选择路径，把每条路径都记录下来。
'''

def subsets(nums):
    res = []
    def backtrack(start, path):
        res.append(path[:])  # 记录当前子集
        for i in range(start, len(nums)):
            path.append(nums[i])         # 入栈：选择nums[i]
            backtrack(i+1, path)         # 递归
            path.pop()                   # 出栈：撤销选择nums[i]
    backtrack(0, [])
    return res


# 子集：像做选择题，每个元素“选/不选”，结果是所有可能的组合。
# 全排列：像洗牌，把所有元素排成一行，顺序不同就算不同。






