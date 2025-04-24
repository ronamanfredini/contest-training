class Solution:
    def findLRSLength(self, str):
        def dfs(i, j):
            if i >= len(str) or j >= len(str):
                return ''
        
            if str[i] == str[j] and i != j:
                return str[i] + dfs(i + 1, j + 1)
            
            path1 = dfs(i + 1, j)
            path2 = dfs(i, j + 1)

            if len(path1) > len(path2):
                return path1
            
            return path2


        return dfs(0, 0)


s = Solution()
print(s.findLRSLength('tomorrow'))
print(s.findLRSLength('aabdbcec'))
print(s.findLRSLength('fmff'))
