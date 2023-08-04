'''
Mapping(?)

Input for example LVIII (58)

L = 50, V= 5, III = 3.

You take each letter and seperate it

L, V, I, I, I

Then use mapping to translate the roman numbers to real numbers

50, 5, 1, 1, 1

And then add them together

Result = 58

'''


class Solution:
    def romanToInt(self, s: str) -> int:

        letter_to_number_mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
}

        s = 'L'
            
        result = letter_to_number_mapping[s]

        return result
    
solution = Solution()

result = solution.romanToInt('L')

print(result)