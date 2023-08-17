from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = float(celsius + 273.15)
        fahrenheit = celsius * 1.80 + 32
        ans = [kelvin, fahrenheit]
        formatted_ans = [format(temp, '.5f') for temp in ans]
        return ans


celsius = 36.50
sol = Solution()
sol.convertTemperature(celsius)