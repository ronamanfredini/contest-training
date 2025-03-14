# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        subsets = []
        unique_sets = set()
        minimum_diff = 999999999
        def dfs(i = 0, set1 = [], set2= []):
            if i >= len(nums):
                set1_as_tuple = tuple(set1)
                set2_as_tuple = tuple(set2)

                if set1_as_tuple not in unique_sets and set2_as_tuple not in unique_sets and len(set1) != 0 and len(set2) != 0:
                    unique_sets.add(set1_as_tuple)
                    unique_sets.add(set2_as_tuple)
                    subsets.append([set1.copy(), set2.copy()])
                return

            num = nums[i]
            set1.append(num)
            dfs(i + 1, set1, set2)
            set1.pop()
            set2.append(num)
            dfs(i + 1, set1, set2)
            set2.pop()

        dfs()

        for set1, set2 in subsets:
            set1_sum = sum(set1)
            set2_sum = sum(set2)
            diff = abs(set1_sum - set2_sum)
            minimum_diff = min(minimum_diff, diff)
        return minimum_diff

s = Solution()
print(s.minimumDifference([-36, 36]))