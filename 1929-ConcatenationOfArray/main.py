from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        sol_list = []
        for number in nums:
            sol_list.append(number)
        sol_list.extend(nums)
        return sol_list


nums = [1,3,2,1]
sol = Solution()
sol.getConcatenation(nums)