import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        if len(piles) > h:
            return False
        if len(piles) == h:
            return piles[-1]

        for i in range(len(piles)):
            remaining = h
            for j in range(len(piles)):
                remaining -= math.ceil(piles[j] / piles[i])
                if remaining >= 0 and j == len(piles) - 1:
                    return piles[i]
                if remaining <= 0:
                    break


s = Solution()
print(s.minEatingSpeed(piles = [3,6,7,8], h = 8))