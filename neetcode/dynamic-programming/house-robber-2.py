from typing import List, Optional

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        if len(nums) < 4:
            return max(nums)

        def dfs(i, took_first):
            if i >= len(nums):
                return 0
            memo_key = (i, took_first)
            if memo_key in memo:
                return memo[memo_key]

            if i == len(nums) - 1 and took_first:
                return 0

            branch1 = dfs(i + 2, took_first) + nums[i]
            if i == 0:
                took_first = False

            branch2 = dfs(i + 1, took_first)
            res = max(branch1, branch2)
            memo[memo_key] = res

            return res

        return max(dfs(0, True), dfs(1, False))

def run_case(nums: List[int], expected: Optional[int] = None) -> None:
    """Run Solution.rob on nums and print got (plus expected/PASS|FAIL if given)."""
    print(f"nums={nums}")
    got = Solution().rob(list(nums))
    if expected is None:
        print(f"  got={got}")
        return
    status = "PASS" if got == expected else "FAIL"
    print(f"  got={got} expected={expected} -> {status}")


# run_case([2, 9, 8, 3, 6], 15)
run_case([5, 1, 2, 6, 12, 7, 9, 3, 4, 10], 33)
