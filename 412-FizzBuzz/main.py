from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        ToBeFilledList = []

        FizzBuzzList = [i for i in range(1, n + 1)]

        print(FizzBuzzList)

        for position in FizzBuzzList:
            print(position)
            ToBeFilledList.append(position)
            if position % 3 == 0 and position % 5 == 0:
                print("FizzBuzz")
                ToBeFilledList.pop(position-1)
                ToBeFilledList.insert(position, "FizzBuzz")
                return ToBeFilledList
            elif position % 5 == 0:
                print("Buzz")
                ToBeFilledList.pop(position-1)
                ToBeFilledList.insert(position, "Buzz")
            elif position % 3 == 0:
                print("Fizz")
                print(position)
                ToBeFilledList.pop(position-1)
                ToBeFilledList.insert(position, "Fizz")

                print(ToBeFilledList)




n = 15
solution = Solution()
solution.fizzBuzz(n)