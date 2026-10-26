class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            m = left + ((right - left) // 2)
            if nums[m] < nums[m - 1] and nums[m] < nums[m + 1]:
                return nums[m]
            elif nums[m] < nums[right]:
                right = m - 1
            elif nums[m] > nums[right]:
                left = m + 1



s = Solution()
print(s.findMin([3,4,5,6,1,2]))
print(s.findMin([4,5,0,1,2,3]))
print(s.findMin([4,5,6,7]))

