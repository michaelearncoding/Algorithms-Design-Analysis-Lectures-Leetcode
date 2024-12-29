
"""

ref: https://leetcode.com/problems/combination-sum/solutions/5426168/video-simply-check-all-combinations/


Type:　recursive / backtracking

# description of the outcome

make_combination adds combinations to the result list res 

only when the current total reaches the target, 

and otherwise it explores the next candidates recursively. 

If the end of the list is reached or if the total exceeds the target, 

the search path is terminated. Ultimately, 

the function returns res containing all valid combinations.

Question:
39. Combination Sum

i.e. 

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


"""

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        res = [] # Step 1: Initialize Result List
        # Create an empty list res to store the final result.

        # Step 2: Define Recursive Function
        # Define a helper function make_combination that
        # takes the current index idx, 
        # current combination comb, 
        # and current total total.
        def make_combination(idx, comb, total):

            # Step 3: Base Case for Valid Combination
            if total == target:
                res.append(comb[:])
                return
            # If the current total equals the target, add a copy of the current combination to res and return.

            # Step 4: Base Case for Invalid Combination
            if total > target or idx >= len(candidates):
                return
            # If the current total exceeds the target or the index goes out of bounds, return.
            
            # Step 5: Include the Current Candidate
            comb.append(candidates[idx])
            make_combination(idx, comb, total + candidates[idx])
            comb.pop()
            # Include candidates[idx] in the combination and recurse with the updated total.
            # Backtrack by removing the last added candidate.

            # Step 6: Exclude the Current Candidate
            make_combination(idx + 1, comb, total)
            # Recurse to the next index without including the current candidate.
            return res 
        
        #Step 7: Initial Call to Recursive Function　：　Start the recursion with index 0, an empty combination list, and a total of 0.
        return make_combination(0, [], 0)



