class Solution:
    def findSPMCount(self, str, pat):
        memo = {}

        def dfs(i, j):
            if j >= len(pat):
                return 1

            if i >= len(str):
                return 0
            
            memo_key = (i, j)
            if memo_key in memo:
                return memo.get(memo_key)
            
            path1 = 0
            if str[i] == pat[j]:
                path1 = dfs(i + 1, j + 1)
            
            path2 = dfs(i + 1, j)

            result = path1 + path2
            memo[memo_key] = result
            return result
        return dfs(0, 0)
    

s = Solution()
print(s.findSPMCount('baxmx', 'ax'))
print(s.findSPMCount('baxmx', 'ax'))
print(s.findSPMCount('tomorrow', 'tor'))
