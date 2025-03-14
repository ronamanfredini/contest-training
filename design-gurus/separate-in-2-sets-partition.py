class Solution:
    def partition(self, nums):
        subsets = []
        unique_sets = set()
        def dfs(i = 0, set1 = [], set2 = []):
            if i >= len(nums):
                if tuple(set1) not in unique_sets and tuple(set2) not in unique_sets:
                    subsets.append([set1.copy(), set2.copy()])
                    unique_sets.add(tuple(set1))
                    unique_sets.add(tuple(set2))
                return

            num = nums[i]
            set1.append(num)
            dfs(i + 1, set1, set2)
            set1.pop()
            set2.append(num)
            dfs(i + 1, set1, set2)
            set2.pop()


        dfs()
        return subsets



s = Solution()
print(s.partition([1,2,3,9]))