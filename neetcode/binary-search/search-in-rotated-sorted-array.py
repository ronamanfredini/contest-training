class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        while left <= right:
            m = left + ((right - left) // 2)

            if nums[m] < nums[m - 1]:
                if nums[m] == target:
                    return m

                elif target > nums[-1]:
                    l = 0
                    r = m - 1
                    while l <= r:
                        mm = l + ((r - l) // 2)
                        if nums[mm] == target:
                            return mm
                        elif nums[mm] < target:
                            l = mm + 1
                        elif nums[mm] > target:
                            r = mm - 1
                    return -1
                elif target > nums[m]:
                    l = m + 1
                    r = len(nums) - 1
                    while l <= r:
                        mm = l + ((r - l) // 2)
                        if nums[mm] == target:
                            return mm
                        elif nums[mm] < target:
                            l = mm + 1
                        elif nums[mm] > target:
                            r = mm - 1
                    return -1
                else:
                    return -1

            elif nums[m] > nums[right]:
                left = m + 1
            elif nums[m] < nums[right]:
                right = m - 1
            

s = Solution()
print(s.search([1,3], 0))