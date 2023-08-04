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
    def __init__(self):
        self.s = 'LV'  # Define s as an instance variable with value 'L'

    def romanToInt(self, n: str) -> int:  # Remove s parameter, since it's an instance variable
        print('roman to int')
        self.s = n
        letter_to_number_mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        total = 0
        previous_value = 0

        for letter in reversed(self.s):
                value = letter_to_number_mapping[letter]
                if value < previous_value:
                     total -= value
                else:
                     total += value
                     previous_value = value
        return total

s = "LVIII"
so = Solution()

i = so.romanToInt(s)

print(f'{i}')