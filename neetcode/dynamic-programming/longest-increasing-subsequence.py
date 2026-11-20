from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        if len(nums) <= 1:
            return 1
        def dfs(i):
            if i  + 1 >= len(nums):
                return 1

            if i in memo:
                return memo.get(i)
            b1 = 0
            if nums[i] < nums[i + 1]:
                b1 = 1 + dfs(i + 1)

            b2 = dfs(i + 1)
            res = max(b1, b2)
            memo[i] = res
            return res
            


        longest = dfs(0)


        return longest

def run_case(nums: List[int]) -> None:
    """Run lengthOfLIS on nums and print the result."""
    print(f"nums={nums}")
    print(f"  got={Solution().lengthOfLIS(nums)}")


run_case([9, 1, 2, 3, 3, 7])
