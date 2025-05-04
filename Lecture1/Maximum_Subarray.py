# Maximum Subarray - Amazon Coding interview Question

# https://www.youtube.com/watch?v=5WZl3MMT0Eg

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Example:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4] 
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Dynamic programming 
class Solution: 
    def maxSubArray(self, nums:list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSub = nums[0]
        curSum = 0
        
        for n in nums:
            if curSum < 0 :
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
    

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(nums, left, right):
            # 基准条件：当只有一个元素时，最大子数组就是该元素本身
            if left == right:
                return nums[left]
            
            # 找到中点
            mid = (left + right) // 2
            
            # 递归计算左半部分和右半部分的最大子数组和
            left_max = helper(nums, left, mid)
            right_max = helper(nums, mid + 1, right)
            
            # 计算跨越中点的最大子数组和
            cross_max = self.cross_sum(nums, left, mid, right)
            
            # 返回三者中的最大值
            return max(left_max, right_max, cross_max)
        
        return helper(nums, 0, len(nums) - 1)
    
    def cross_sum(self, nums, left, mid, right):
        # 计算左半部分的最大和（从中点向左扩展）
        left_sum = float('-inf')
        cur_sum = 0
        for i in range(mid, left - 1, -1):
            cur_sum += nums[i]
            left_sum = max(left_sum, cur_sum)
        
        # 计算右半部分的最大和（从中点向右扩展）
        right_sum = float('-inf')
        cur_sum = 0
        for i in range(mid + 1, right + 1):
            cur_sum += nums[i]
            right_sum = max(right_sum, cur_sum)
        
        # 返回跨越中点的最大和
        return left_sum + right_sum