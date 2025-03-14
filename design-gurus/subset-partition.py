class Solution:
    def partition(self, nums):
        subsets = []
        def dfs(i = 0, current_set = []):
            if i >= len(nums):
                subsets.append(current_set.copy())
                return

            current_set.append(nums[i])
            dfs(i + 1, current_set)
            current_set.pop()
            dfs(i + 1, current_set)

        dfs()


        return subsets



s = Solution()
print(s.partition([1,2,3,9]))