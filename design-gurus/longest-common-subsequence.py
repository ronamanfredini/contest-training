class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            memo_key = (i, j)

            if memo_key in memo:
                return memo.get(memo_key)

            if text1[i] == text2[j]:
                result = dfs(i + 1, j + 1) + 1
                memo[memo_key] = result
                return result
            
            remainder = max(dfs(i + 1, j), dfs(i, j + 1))
            memo[memo_key] = remainder
            return remainder

        return dfs(0, 0)   

s = Solution()
print(s.longestCommonSubsequence('abcde', 'ace'))
        