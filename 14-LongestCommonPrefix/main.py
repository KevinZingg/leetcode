'''
Array of words -> Find out until when their letters are the same

Input: strs = ["flower","flow","flight"]
Output: "fl"

Separate letters of each word

flower = f, l, o, w, e, r
flow = f, l, o, w
...

Take the longest word.

take each letter and compare it to the other letters

f-l-o-w-e-r
T-T-F-F-F-F (True = Same Letter / F = Not Same Letter)
f-l-i-g-h-t


B-B-A-A-A-B-B
T-F-F-T-T-F-F (True = Same Letter / F = Not Same Letter)
B-A-B-A-A-B-A

print longest segment of true letters:

B-B-A-A-A-B-B (Word)
T-F-F-T-T-F-F (True = Same Letter / F = Not Same Letter)
B-A-B-A-A-B-A (Word)



'''
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = ["flower","flow","flight"] #["dog","racecar","car"]
        first_word = strs[0]

        for first_word_letter in first_word:
            amount_of_items = 0

            for word in strs:
                amount_of_items += 1
                for letter in word:
                    if letter == first_word_letter and amount_of_items == len(strs):
                        print(letter)
                    elif amount_of_items < len(strs):
                        print("There is no common prefix among the input strings.")

        print(strs)

solution = Solution()

solution.longestCommonPrefix([])