from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # If the timeSeries is empty, then the total time poisoned is 0
        if not timeSeries:
            return 0

        poisonedTime = 0

        # Iterate over all the attacks
        for i in range(1, len(timeSeries)):
            # Calculate the time between current attack and previous one
            timeDifference = timeSeries[i] - timeSeries[i - 1]
            # If the time difference is less than the duration, add it to poisoned time
            poisonedTime += min(timeDifference, duration)

        # For the last attack, add full duration
        poisonedTime += duration

        return poisonedTime


# Test
timeSeries = [1, 4]
duration = 2

sol = Solution()
print(sol.findPoisonedDuration(timeSeries, duration))  # It should print 3
