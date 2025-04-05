class Solution:
    memo = {}
    def countWays(self, n):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if n == 1:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        if n in self.memo:
            return self.memo.get(n)
        
        result = self.countWays(n - 1) + self.countWays(n - 3) + self.countWays(n - 4)
        self.memo[n] = result

        return result

s = Solution()
print(s.countWays(5))