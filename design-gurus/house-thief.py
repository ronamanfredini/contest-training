class Solution:
    def findMaxSteal(self, wealth):
        memo = {}
        def dfs(i):
            if i >= len(wealth):
                return 0
            
            memo_key = i
            if memo_key in memo:
                return memo.get(memo_key)
            
            skip_current = dfs(i + 1)
            current_element = wealth[i]
            take_current = dfs(i + 2) + current_element

            result = max(skip_current, take_current)
            memo[memo_key] = result

            return result

        return dfs(0)


s = Solution()
print(s.findMaxSteal([2, 5, 1, 3, 6, 2, 4]))