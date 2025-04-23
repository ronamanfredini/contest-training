class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        memo = {}
        def dfs(i, j):
            if i == len(str1):
                return str2[j:]
            if j == len(str2):
                return str1[i:]

            memo_key = (i, j)
            if memo_key in memo:
                return memo.get(memo_key)

            if str1[i] == str2[j]:
                result = str1[i] + dfs(i + 1, j + 1)
                memo[memo_key] = result

                return result

            path1 = str1[i] + dfs(i + 1, j)
            path2 = str2[j] + dfs(i, j + 1)

            if len(path1) < len(path2):
                memo[memo_key] = path1
                return path1

            memo[memo_key] = path2
            return path2
        return dfs(0, 0)

s = Solution()
# print(s.shortestCommonSupersequence('abac', 'cab'))
# print(s.shortestCommonSupersequence('abc', 'ahbgdc'))
print(s.shortestCommonSupersequence('aca', 'aba'))