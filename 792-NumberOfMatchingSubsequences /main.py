from typing import List
import itertools

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        counter = 0

        results = set()  # Using a set to avoid duplicates

        # Get all substrings of 's' and their permutations
        for length in range(1, len(s) + 1):
            for i in range(len(s) - length + 1):
                substring = s[i:i + length]
                for perm in itertools.permutations(substring):
                    results.add(''.join(perm))

        # Convert set to list
        results = list(results)
        print(results)

        for word in results:
            if word in words:
                counter += 1
        int(counter)
        print(counter)
        return counter


s = "abcde"
words = ["a", "bb", "acd", "ace"]
sol = Solution()
sol.numMatchingSubseq(s, words)