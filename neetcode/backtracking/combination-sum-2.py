from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        unique = list(set(candidates))
        freq_map = {}
        result = []
        for num in candidates:
            freq_map[num] = freq_map.get(num, 0) + 1

        def dfs(nums, freq, i, curr_arr, curr_sum):
            if target == curr_sum:
                result.append(curr_arr.copy())
                return
            if i >= len(nums) or curr_sum > target:
                return
            
            num = nums[i]
            if freq.get(num) > 0:
                freq[num] -= 1
                curr_arr.append(num)
                curr_sum += num
                dfs(nums, freq, i, curr_arr, curr_sum)
                curr_sum -= num 
                curr_arr.pop()
                freq[num] += 1
            dfs(nums, freq, i + 1, curr_arr, curr_sum)



        dfs(unique, freq_map, 0, [], 0)


        return result
        

def run_case(candidates: List[int], target: int) -> None:
    """Run combinationSum2 on one case and print the result."""
    print(f"candidates={candidates} target={target}")
    got = Solution().combinationSum2(candidates, target)
    print(f"  got={got}")


run_case([9, 2, 2, 4, 6, 1, 5], 8)
