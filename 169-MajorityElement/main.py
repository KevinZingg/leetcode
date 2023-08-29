from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        counter_dict = {}

        for number in nums:
            if number not in counter_dict:
                counter_dict[number] = 1
            elif number in counter_dict:
                counter_dict[number] += 1

        most_appeared = max(counter_dict.values())
        most_appeared = str(most_appeared)


        for key, value in counter_dict.items():
            if str(value).startswith(most_appeared):
                print(key)
                return key





nums = [3, 2, 3]
sol = Solution()
sol.majorityElement(nums)