from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        counter = 0
        sol_list = []

        for level in triangle:
            min_value = min(level)
            print(min_value)
            sol_list.append(min_value)
            print(sol_list)

        triangle_sum = sum(sol_list)
        print(triangle_sum)
        return triangle_sum


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
sol = Solution()
sol.minimumTotal(triangle)