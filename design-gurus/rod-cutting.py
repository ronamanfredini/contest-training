class Solution:
    def solveRodCutting(self, lengths, prices, n):
        memo = {}
        def dfs(i = 0, length = n):
            if i >= len(lengths):
                return 0
            
            if length == 0:
                return 0
            
            memo_key = (i, length)
            if memo_key in memo:
                return memo.get(memo_key)
            
            current_length = lengths[i]
            current_price = prices[i]

            skip_current = dfs(i + 1, length)

            take_current = 0
            if current_length <= length:
                take_current = dfs(i, length - current_length) + current_price

            result = max(take_current, skip_current)
            memo[memo_key] = result

            return result
        return dfs()
    

s = Solution()
print(s.solveRodCutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13],5))
