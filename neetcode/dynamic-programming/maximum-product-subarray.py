from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg_count = 0

        for num in nums:
            if num < 0:
                neg_count += 1

        first_non_zero = 0
        for num in nums:
            if num != 0:
                break
            first_non_zero += 1
        left = first_non_zero
        curr = nums[left]
        if curr < 0:
            neg_count -= 1
        res = curr
        if left + 1 >= len(nums):
            return nums[-1]
        for right in range(left + 1, len(nums)):
            res = max(res, nums[right])
            if nums[right] != 0:
                temp = nums[right] * curr
                if nums[right] < 0:
                    neg_count -= 1

                res = max(res, curr, temp)
                if temp >= curr:
                    curr = temp
                    continue
                
                if neg_count > 0:
                    curr = temp
                    continue
            
            while left < right:
                if nums[left] != 0:
                    curr = curr / nums[left]
                if nums[left] < 0:
                    neg_count += 1
                left += 1
            
        return int(res)
                


def run_case(nums: List[int]) -> None:
    """Run maxProduct on nums and print the result."""
    print(f"nums={nums}")
    print(f"  got={Solution().maxProduct(nums)}")


run_case([-3, 0, -2])
