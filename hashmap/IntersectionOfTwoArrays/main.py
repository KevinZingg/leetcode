from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        doubles = []

        for number in nums1:
            if number in nums2:
                doubles.append(number)
        doubles = list(dict.fromkeys(doubles))
        return doubles

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

sol = Solution()
sol.intersection(nums1, nums2)