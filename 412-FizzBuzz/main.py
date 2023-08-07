from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ToBeFilledList = []
        FizzBuzzList = [i for i in range(1, n + 1)]
        for position in FizzBuzzList:
            ToBeFilledList.append(position)
            if position % 3 == 0 and position % 5 == 0:
                ToBeFilledList.pop(position-1)
                ToBeFilledList.insert(position, "FizzBuzz")
            elif position % 5 == 0:
                ToBeFilledList.pop(position-1)
                ToBeFilledList.insert(position, "Buzz")
            elif position % 3 == 0:
                ToBeFilledList.pop(position-1)
                ToBeFilledList.insert(position, "Fizz")
            n = ToBeFilledList
            n = [str(item) for item in n]
        return n


n = 15
solution = Solution()
solution.fizzBuzz(n)