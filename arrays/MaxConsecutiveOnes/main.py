from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_count = 0

        for number in nums:
            if number == 1:
                counter += 1
                max_count = max(max_count, counter)
            else:
                counter = 0

        return(max_count)

nums = [1, 1, 1, 0, 0, 1, 0, 1]

solution = Solution()
solution.findMaxConsecutiveOnes(nums)


'''
check current number with next one
if same then +1 to itterator variable
if not same -> save itteration-value in array
at the end get largest number from array
'''