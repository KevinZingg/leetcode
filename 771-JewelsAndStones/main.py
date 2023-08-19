class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        count = 0
        jewel_map = {}
        for jewel in jewels:
            jewel_map[jewel] = True
        for stone in stones:
            if stone in jewel_map:
                count += 1
        return count


jewels = "aA"
stones = "aAAbbbb"

sol = Solution()
sol.numJewelsInStones(jewels, stones)