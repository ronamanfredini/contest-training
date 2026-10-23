class Solution:
    def trap(self, height: list[int]) -> int:
        max_area = 0
        local_area = 0
        l = 0
        for r in range(len(height)):
            if height[r] >= height[l]:
                l = r
                max_area += local_area
                local_area = 0
            
            local_area += height[l] - height[r]
        return max_area
    
s = Solution()
# print(s.trap([0,1,0,2,1,0,1,3,2,1,2,4])) # 10
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
