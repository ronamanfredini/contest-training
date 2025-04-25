class Solution:
    def findLASLength(self, nums):
        memo = {}
        def dfs(i, last_index, last_direction = None):
            UP = 'up'
            DOWN = 'down'

            if i >= len(nums):
                return 0
            
            memo_key = (i, last_index, last_direction)
            if memo_key in memo:
                return memo.get(memo_key)
            
            if last_index == -1:
                result1 = dfs(i + 1, i, UP) + 1
                result2 = dfs(i + 1, i, DOWN) + 1
                result = max(result2, result1)
                memo[memo_key] = result
                return result

            current_num = nums[i]
            prev_num = nums[last_index]

            skip_path = dfs(i + 1, last_index, last_direction)
            take_path = 0
            if last_direction == UP:
                if current_num < prev_num:
                    take_path = dfs(i + 1, i, DOWN) + 1
            if last_direction == DOWN:
                if current_num > prev_num:
                    take_path = dfs(i + 1, i, UP) + 1
            
            result = max(take_path, skip_path)
            memo[memo_key] = result
            return result
                

        return dfs(0, -1, None)


s = Solution()
print(s.findLASLength([1, 2, 3, 4]))
print(s.findLASLength([3, 2, 1, 4]))
print(s.findLASLength([1, 3, 2, 4]))
print(s.findLASLength([4, 3, 2, 1]))