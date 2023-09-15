from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        print(s)
        words_list = []
        result_string = ""
        s.strip(" ")


        sentence_list = s.split()
        for word in sentence_list:
            words_list.append(word)

        print(words_list)

        words_list.reverse()

        print(words_list)

        for word in words_list:
            result_string += word + " "

        result_string = result_string.strip(" ")
        print(f"-{result_string}-")
        return result_string



s = "the sky is blue"

sol = Solution()
sol.reverseWords(s)