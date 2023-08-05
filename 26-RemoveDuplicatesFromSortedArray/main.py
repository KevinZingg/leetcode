'''

Itterate

'''

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(set(nums)) < len(nums):
            print("There's a dupe!")


nums = [1, 1, 2]

solution = Solution()

solution = solution.removeDuplicates(nums)