'''
Cleared in 10 minutes, very cool :D

nvm solution went crazy...

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(acc) for acc in accounts])
'''


from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        empty_array = []
        for account in accounts:
            summe = sum(account)
            empty_array.append(summe)
        richest = max(empty_array)
        return richest


accounts = [[1,5],[7,3],[3,5]]
solution = Solution()
solution.maximumWealth(accounts)