from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        square_list = []

        for number in nums:
            square = number * number
            square_list.append(square)
            square_list.sort()
        return square_list

nums = [-4, -1, 0, 3, 10]

solution = Solution()
solution.sortedSquares(nums)