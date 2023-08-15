from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        res = []
        [res.append(items) for items in nums if items not in res]
        if len(res) != len(nums):
            return True
        elif len(res) == len(nums) :
            return False

nums = [1,1,2,3,4]

solution = Solution()

solution.containsDuplicate(nums)