class Solution:
    def findMinOperations(self, s1, s2):
        def dfs(i, j, str):
            if len(s1) == 0:
                return len(s2)

            if len(s2) == 0:
                return len(s1)
            
            if str == s2:
                return 0

            if i >= len(s1):
                return abs(len(str) - abs(len(s2)))
            
            if j >= len(s2):
                return abs(len(str) - abs(len(s1)))

            if s1[i] == s2[j]:
                return dfs(i + 1, j + 1, str + s1[i]) + 1
            
            insert_path = dfs(i, j + 1, str + s2[j]) + 1
            delete_path = dfs(i + 1, j, str) + 1
            replace_path = dfs(i + 1, j + 1, str + s2[j]) + 1

            result = min(insert_path, delete_path, replace_path)

            return result
            

            


        return dfs(0, 0, '')
s = Solution()
print(s.findMinOperations('bat', 'but'))
print(s.findMinOperations('abdca', 'cbda'))
print(s.findMinOperations('aca', 'acda'))
print(s.findMinOperations('passpot', 'ppsspqrt'))
print(s.findMinOperations('abc', ''))