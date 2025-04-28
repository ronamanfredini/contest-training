class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_element_count = len(nums)
        total = sum(nums)
        if total < target:
            return 0

        left = 0
        right = 0
        curr_sum = 0

        for right in range(len(nums)):
            current_num = nums[right]
            curr_sum += current_num

            while curr_sum >= target:
                curr_arr_len = right - left + 1
                min_element_count = min(min_element_count, curr_arr_len)
                curr_sum -= nums[left]
                left += 1
        
        return min_element_count

s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.minSubArrayLen(213, [12,28,83,4,25,26,25,2,25,25,25,12]))