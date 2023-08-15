from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        test_list = []

        for number in arr:
            test_list.append(number)
            if number == 0:
                test_list.append(0)


        # Modify the original list in place
        arr[:] = test_list[:len(arr)]

        return arr  # This return is optional since you're modifying the original list in place

arr = [1,0,2,3,0,4,5,0]
solution = Solution()