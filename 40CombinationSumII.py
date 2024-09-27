"""
40. Combination Sum II

Question:

Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.




"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort Candidates:
        candidates.sort()
        # Sorts the candidates list in non-decreasing order. 
        # This is crucial for ensuring that duplicates can be handled effectively 
        # and combinations are generated in a predictable manner.
        
        # Initialize Result List:
        res = []
        # Initializes an empty list res to store all valid combinations that sum up to target.

        # Define Depth-First Search (DFS) Function dfs:
        # Parameters:
        # target: Current remaining target sum to achieve.
        # start: Index to start exploring in the candidates list.
        # comb: Current combination being constructed
        #

        def dfs(target, start, comb):
            # base cases
            # Checks if target is less than 0. If true, 
            # it means the current combination cannot lead to a valid sum, 
            # so the function returns without further exploration
            #
            # Checks if target equals 0. If true, 
            # it means comb sums up to the target, 
            # so comb is added to res, and the function returns.
            #
            if target < 0:
                return
            if target == 0:
                res.append(comb)
                return
            for i in range(start, len(candidates)):
                # Iterate through Candidates:
                # Iterates through the candidates list starting from index start. 
                # This loop explores all possible candidates to include in the current combination.
                #
                ##
                if i > start and candidates[i] == candidates[i-1]:
                    continue # Skips duplicates to avoid generating duplicate combinations.
                             # This condition ensures that only the first occurrence of each candidate value at any depth of recursion is considered.
                if candidates[i] > target: # Check Candidate Value:
                    break # Breaks out of the loop if the current candidate value exceeds the remaining target. Since candidates is sorted, 
                          # all subsequent values will also be greater than target.
                dfs(target-candidates[i], i+1, comb+[candidates[i]])
                # Updated target by subtracting candidates[i].
                # Updated start to i + 1 to avoid reusing the same element.
                # Updated comb by adding candidates[i] to it, 
                # representing the current combination being explored.


        dfs(target, 0, []) # Initiates the depth-first search by calling dfs with the initial parameters: target (the original target sum), 0 (starting index in candidates), and an empty list [] (initial empty combination). 
        return res # Returns the list res containing all valid combinations found during the depth-first search process.
    
