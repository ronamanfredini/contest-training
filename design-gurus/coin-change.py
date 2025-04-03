class Solution:
    def countChange(self, denominations, total):
        memo = {}
        def dfs(i = 0, total = total):
            if i >= len(denominations):
                return 0
            
            if total == 0:
                return 1
            
            memo_key = (i, total)
            if memo_key in memo:
                return memo.get(memo_key)
            
            skip_current = dfs(i + 1, total)
            current_coin = denominations[i]

            take_current = 0
            if current_coin <= total:
                take_current = dfs(i, total - current_coin)

            combinations = skip_current + take_current
            memo[memo_key] = combinations

            return combinations
        return dfs()

s = Solution()
print(s.countChange([1, 2, 3], 5))
