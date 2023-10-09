from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for number in nums:
            if number in seen:
                print(number)
                return True
            else:
                seen.add(number)

        return False

nums = [1, 2, 3, 4, 3]

sol = Solution()
sol.containsDuplicate(nums)