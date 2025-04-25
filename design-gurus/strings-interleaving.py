class Solution:
    def findSI(self, m, n, p):
        if len(m + n) > len(p):
            return False

        def is_subsequence(str1, str2):
            curr_char_count = [0]
            def dfs(i, j):
                if i >= len(str1):
                    return False
                
                if j >= len(str2):
                    return False
                
                if curr_char_count[0] == len(str1):
                    return
                
                if str1[i] ==  str2[j]:
                    curr_char_count[0] += 1
                    return dfs(i + 1, j + 1)
                
                return dfs(i, j + 1)

            dfs(0, 0)
            return curr_char_count[0] == len(str1)
            



        return is_subsequence(m, p) and is_subsequence(n, p)

s = Solution()
print(s.findSI('abd', 'cef', 'abcdef'))
print(s.findSI('abd', 'cef', 'abcbef'))
print(s.findSI('abcdef', 'mnop', 'mnaobcdepf'))