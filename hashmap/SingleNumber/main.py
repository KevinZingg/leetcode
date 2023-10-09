from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        
        for number in nums:
            if number in dict:
                dict[number] += 1
            else:
                dict[number] = 1
        lonelyNumber = [key for key, value in dict.items() if value == 1]
        lonelyNumber = lonelyNumber[0]
        return lonelyNumber


nums = [4, 1, 2, 1, 2]

sol = Solution()
sol.singleNumber(nums)