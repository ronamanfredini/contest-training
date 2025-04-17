class Solution:
    max_substring_len = 0
    def findLCSLength(self, s1, s2):
        memo = {}
        def dfs(i, j, curr_substring_len = 0):
            if i >= len(s1) or j >= len(s2):
                return 0
            
            if s1[i] == s2[j]:
                curr_substring_len += 1
                next_result = dfs(i + 1, j + 1, curr_substring_len)
                result = max(next_result, curr_substring_len)
                self.max_substring_len = max(self.max_substring_len, result)
                return result
            
            result1 = dfs(i + 1, j)
            result2 = dfs(i, j + 1)

            result = max(result1, result2)
            self.max_substring_len = max(result, self.max_substring_len)

            return 0
            
        dfs(0, 0)
        return self.max_substring_len



s = Solution()
print(s.findLCSLength('abdca', 'cbda'))
print(s.findLCSLength('passport', 'ppsspt'))
