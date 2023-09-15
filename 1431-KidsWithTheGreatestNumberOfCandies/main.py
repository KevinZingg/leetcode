from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return_list = []

        for person in candies:
            candy_per_person = person + extraCandies
            if all(candy_per_person > x or candy_per_person == x for x in candies):
                return_list.append(True)
            else:
                return_list.append(False)

        return return_list


candies = [2, 3, 5, 1, 3]
extraCandies = 3

sol = Solution()
result = sol.kidsWithCandies(candies, extraCandies)
print(result)
