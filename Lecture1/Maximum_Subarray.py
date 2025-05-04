# Maximum Subarray - Amazon Coding interview Question

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Example:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4] 
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

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