class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        sol_list = []
        list_word1 = [i for i in word1]
        list_word2 = [i for i in word2]


        min_len = min(len(list_word1), len(list_word2))

        for letter in range(min_len):
            sol_list.append(letter)
            print(sol_list)

        print(list_word1)

word1 = "abc"
word2 = "xyz"

solution = Solution()
solution.mergeAlternately(word1,word2)