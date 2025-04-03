import math
class Solution:
    def countRibbonPieces(self, ribbonLengths, total):
        memo = {}
        def dfs(i = 0, total = total):
            if i >= len(ribbonLengths):
                return -math.inf

            if total == 0:
                return 0
            
            memo_key = (i, total)
            if memo_key in memo:
                return memo.get(memo_key)

            skip_current = dfs(i + 1, total)
            current_len = ribbonLengths[i]

            take_current = -math.inf
            if current_len <= total:
                take_current = dfs(i, total - current_len) + 1
            
            result = max(take_current, skip_current)
            memo[memo_key] = result

            return result

        return dfs()

s = Solution()
print(s.countRibbonPieces([2,5, 7], 13))