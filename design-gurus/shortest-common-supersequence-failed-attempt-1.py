class Solution:
    def is_subsequence(self, str1, str2) -> bool:
        char_counter = [0]
        memo = {}
        def is_subsequence_dfs(i, j):
            if char_counter[0] == len(str1): 
                return True
            
            if i >= len(str1) or j >= len(str2):
                return False
            
            memo_key = (i, j)
            if memo_key in memo:
                return memo.get(memo_key)
            
            if str1[i] == str2[j]:
                char_counter[0] += 1
                result = is_subsequence_dfs(i + 1, j + 1)
                memo[memo_key] = result

                return result
            
            result = is_subsequence_dfs(i, j + 1)
            memo[memo_key] = result
            return result

        if str1 == str2:
            return True

        if len(str1) > len(str2):
            return False
        
        return is_subsequence_dfs(0, 0)

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        joined_strings = str1 + str2
        str1_str2_max = max(len(str1), len(str2))
        current_min = [joined_strings]

        def dfs(str):
            if len(str) == 0 or len(str) < str1_str2_max:
                return
            
            if self.is_subsequence(str1, str) and self.is_subsequence(str2, str):
                if len(str) < len(current_min[0]):
                    current_min[0] = str
            
            for i in range(len(str)):
                dfs(str[:i] + str[i + 1:])

        dfs(joined_strings)
        return current_min
    
s = Solution()
print(s.is_subsequence('abac', 'cab'))
print(s.is_subsequence('abc', 'ahbgdc'))