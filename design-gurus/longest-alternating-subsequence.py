class Solution:
    def findLASLength(self, nums):
        def dfs(i, last_index = -1, should_increase = False):
            if i >= len(nums):
                return 0

            current_num = nums[i]
            last_num = nums[last_index]
            skip_path = dfs(i + 1, last_index, should_increase)

            take_path = 0
            if last_index == -1:
                take_path = max(dfs(i + 1, i, False) + 1, dfs(i + 1, i, True) + 1)
            if should_increase and current_num > last_num:
                take_path = dfs(i + 1, i, False) + 1
            elif not should_increase and current_num < last_num:
                take_path = dfs(i + 1, i, True) + 1

            result = max(skip_path, take_path)
            return result

        return dfs(0)


s = Solution()
# print(s.findLASLength([1, 2, 3 , 4]))
print(s.findLASLength([3, 2, 1, 4]))
# print(s.findLASLength([1, 3, 2 ,4]))
# print(s.findLASLength([4, 3, 2, 1]))