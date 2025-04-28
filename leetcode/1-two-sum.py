class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        remainder_map = {}

        for i in range(len(nums)):
            curr_num = nums[i]
            if curr_num in remainder_map:
                return [i, remainder_map.get(curr_num)]
            
            remainder = target - curr_num
            remainder_map[remainder] = i
        
