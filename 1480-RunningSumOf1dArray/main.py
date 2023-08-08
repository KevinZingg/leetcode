from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        empty_array = []
        final_array = []
        postition = -1

        for letter in nums:
            postition += 1
            if postition == 0:
                empty_array.append(letter)
                final_array.append(letter)
            elif postition <= len(nums):
                empty_array.append(letter)
                current_sum = sum(empty_array)
                final_array.append(current_sum)
                print(current_sum)
                print(final_array)
        return final_array


nums = [3, 1, 2, 10, 1]
solution = Solution()
solution.runningSum(nums)


'''
        for letter in nums:
            postition += 1
            if postition == 0:
                empty_array.append(letter)
                print("1. letter")
            elif postition <= len(nums):
                print(f"Letter {letter}")
                current_added = nums[postition-1] + letter
                print(f"Current addition {current_added}")
'''