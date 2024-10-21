#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#


# Ref:Subsets II - Backtracking - Leetcode 90 - Python
# https://www.youtube.com/watch?v=Vn2v6ajA7U0


# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset): 
        # It's like the bottome of the tree
        # subset is the current subset

            if i == len(nums): 
                # if the tracker equals to the lengthen of the list
                res.append(subset[::])
                return # end the current level of future outcomes
            
            # All subsets that include nums[i] - (1)pick it or (2)skip it
            subset.append(nums[i])
            backtrack(i + 1, subset) # key part 
            subset.pop()

            # All subsets that do not include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset) # key part 

        backtrack(0, [])
        return res

        
# @lc code=end

