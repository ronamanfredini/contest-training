class Solution:
    def countWays(self, n):
        memo = {}

        def dfs(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n == 3:
                return 4

            if n in memo:
                return memo.get(n)

            result = dfs(n - 1) + dfs(n - 2) + dfs(n - 3)
            memo[n] = result
            return result

        return dfs(n)
