'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

PLAN:

separate nums in to single numbers

calculate "target - nums[n]"

if resultet number is contained in the array (and is not itself) then we know what two number add to become the target

Then find out their position (itterate through them)

output them

'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numbers_in_num = 0
        for e, number in enumerate(nums):
            print(e, number)


            skip = e
            sum = target

            for n in nums:
                if skip > 0:
                    skip -= 1
                    continue



                sum = sum - n
                print(f"Result: {sum}")

                if sum == 0:
                    print(f"AAAAAAAAAA {e} {n}")



                #if target - n == 0
                print(f" n {n}")

            solution_list.append(e)
            # return solution_list

nums = [3,2,4]
target = 6
solution_list = []

solution = Solution()

solution.twoSum(nums, target)

print(solution_list)