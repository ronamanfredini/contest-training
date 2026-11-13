from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        unique = list(set(nums))
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        def dfs(nums, freq, i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            num = nums[i]
            if freq[num] > 0:
                curr.append(num)
                freq[num] -= 1
                dfs(nums, freq, i, curr)
                curr.pop()
                freq[num] += 1
            
            dfs(nums, freq, i + 1, curr)

        
        dfs(unique, freq, 0, [])
        return res

def run_case(nums: List[int]) -> None:
    """Run subsetsWithDup on nums and print the result."""
    print(f"nums={nums}")
    print(f"  got={Solution().subsetsWithDup(nums)}")


run_case([1, 2, 1])
