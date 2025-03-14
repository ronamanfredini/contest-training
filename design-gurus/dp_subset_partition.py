class Solution:
    def canPartition(self, num):
        self.is_possible = False
        subsets = set()

        def dfs(i=0, current_sum=0):
            if i >= len(num):
                if current_sum in subsets:
                    self.is_possible = True
                subsets.add(current_sum)
                return

            current_num = num[i]
            dfs(i + 1, current_sum + current_num)
            dfs(i + 1, current_sum)

        dfs()
        return self.is_possible


s = Solution()
print(s.canPartition([2, 3, 4, 6]))
# s = Solution()

# print(s.canPartition([1,1,3,4,7]))