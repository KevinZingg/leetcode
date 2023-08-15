from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        counter = 0

        for number in nums:
            length = (len(str(number)))
            if length % 2 == 0:
                counter += 1
        return counter


nums = [12, 345, 2, 6, 7896]

solution = Solution()
solution.findNumbers(nums)