import re

class Solution:
    def defangIPaddr(self, address: str) -> str:

        newAddress = re.sub("[.]", "[.]", address)
        return newAddress


address = "1.1.1.1"
sol = Solution()
sol.defangIPaddr(address)