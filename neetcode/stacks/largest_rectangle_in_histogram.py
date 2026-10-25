class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i in range(len(heights)):
            while len(stack) > 0 and stack[-1][0] > heights[i]:
                top = stack.pop()
                area = top[0] *  (i - top[1])
                max_area = max(max_area, area)
                stack.append((heights[i], top[1]))
            stack.append((heights[i], i))

        while len(stack) > 0:
            top = stack.pop()
            area = top[0] * (len(heights) - top[1])
            max_area = max(area, max_area)

        

        return max_area

s = Solution()

print(s.largestRectangleArea([7,1,7,2,2,4]))