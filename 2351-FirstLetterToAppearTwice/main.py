class Solution:
    def repeatedCharacter(self, s: str) -> str:

        letter_dict = {}

        for letter in s:
            if letter in letter_dict:
                letter_dict[letter] += 1
                if letter_dict[letter] == 2:
                    print(letter)
                    return letter


            else:
                letter_dict[letter] = 1


s = "abccbaacz"
sol = Solution()
sol.repeatedCharacter(s)