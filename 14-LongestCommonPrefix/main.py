from typing import List
import re
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return "There is no common prefix"

        strs.sort()

        first = strs[0]
        last = strs[-1]

        i = 0

        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]


strs = ["flower", "flow", "flight"] #["dog","racecar","car"]

solution = Solution()

solution.longestCommonPrefix([])