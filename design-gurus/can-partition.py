class Solution:
    def canPartition(self, num):
        memo = {}
        def dfs(set1Sum = 0, set2Sum = 0, i = 0):
            if i >= len(num):
                if set1Sum == set2Sum:
                    return True

                return False

            memo_key = (i, set1Sum, set2Sum)
            if memo_key in memo:
                return memo.get(memo_key)
            
            current_num = num[i]
            path1 = dfs(set1Sum + current_num, set2Sum, i + 1)
            path2 = dfs(set1Sum, set2Sum + current_num, i + 1)


            result = path1 or path2
            memo[memo_key] = result

            return result
        return dfs()


s = Solution()
print(s.canPartition([1, 2, 3 ,4]))
print(s.canPartition([2,3,4,6]))