class Solution:
    def findMDI(self, s1, s2):
        memo = {}
        def dfs(i = 0, j = 0):
            memo_key = (i, j)
            if i >= len(s1) and j >= len(s2):
                return 0
            if i >= len(s1) or j >= len(s2):
                return abs(len(s1) - len(s2))
            
            if memo_key in memo:
                return memo.get(memo_key)
            
            should_sum = 0 if s1[i] == s2[j] else 1

            result = dfs(i + 1, j + 1) + should_sum
            memo[memo_key] = result

            return result

        return dfs()


s = Solution()
print(s.findMDI('abc', 'fbc'))
print(s.findMDI('abdca', 'cbda'))
print(s.findMDI('passport', 'ppsspt'))