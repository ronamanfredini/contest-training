class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []


        for i in range(0, len(nums), 1):
            right = len(nums) - 1
            left = i + 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while left < right:
                if left == i:
                    left += 1
                    continue
                if right == i:
                    right -= 1
                    continue

                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum > 0:
                    right -= 1

                elif current_sum < 0:
                    left += 1
                
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and left > 0 and nums[left] == nums[left - 1]:
                        left += 1

        return result

                               
                




            
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))