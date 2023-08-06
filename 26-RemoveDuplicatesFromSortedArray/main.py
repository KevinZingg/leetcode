from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # handle empty list
            return 0

        idx = 0  # a pointer to track the position in the original list

        # Loop through the list and place unique elements at the beginning
        for num in nums:
            if idx == 0 or nums[idx - 1] != num:
                nums[idx] = num
                idx += 1

        # The unique numbers are in the list nums[:idx]
        return idx  # Return the number of unique elements

nums = [0, 1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 6]
solution = Solution()
length = solution.removeDuplicates(nums)
print(nums[:length])  # Output will be [0, 1, 2, 3, 4, 5, 6]
