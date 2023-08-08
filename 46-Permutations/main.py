from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(remaining, current_permuatation):
            if not remaining:
                results.append(current_permuatation[:])
            

        results = []

nums = [1, 2, 3]
solution = Solution()
solution.permute(nums)