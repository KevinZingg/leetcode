class Solution:
    def finalString(self, s: str) -> str:

        temp_list = []
        temp_s = ""

        for letter in s:
            if letter != "i":
                temp_list.append(letter)
            elif letter == "i":
                temp_list = temp_list[::-1]

        s = temp_s.join(temp_list)
        print(s)
        return s

s = "string"

solution = Solution()

solution.finalString(s)