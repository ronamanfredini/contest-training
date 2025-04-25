class Solution:
    def findLBSLength(self, nums):
        memo = {}
        def dfs(i, last_index = -1, last_direction = None):
            UP = 'up'
            DOWN = 'down'

            if i >= len(nums):
                return 0

            memo_key = (i, last_index, last_direction)
            if memo_key in memo:
                return memo.get(memo_key)

            if last_index == -1:
                path1 = dfs(i + 1, i, UP) + 1
                # path2 = dfs(i + 1, i, DOWN) + 1
                path2 = 0
                result = max(path1, path2)

                memo[memo_key] = result
                return result
            
            current_num = nums[i]
            last_num = nums[last_index]

            skip_path = dfs(i + 1, last_index, last_direction)
            take_path = 0
            if last_direction == UP:
                if current_num > last_num:
                    path1 = dfs(i + 1, i, UP) + 1
                    # path2 = dfs(i + 1, i, DOWN) + 1
                    path2 = 0
                    take_path = max(path1, path2)
                if current_num < last_num:
                    take_path = dfs(i + 1, i, DOWN) + 1

            if last_direction == DOWN:
                if current_num < last_num:
                    take_path = dfs(i + 1, i, DOWN) + 1
            
            result = max(skip_path, take_path)
            memo[memo_key] = result
            return result
            
        return dfs(0)
    
s = Solution()
print(s.findLBSLength([4,3,2,1])) # result = 4
print(s.findLBSLength([1,3,6,7,9,4,10,5,6])) # result = 5
print(s.findLBSLength([4,2,3,6,10,1,12])) # result = 5
print(s.findLBSLength([4,2,5,9,7,6,10,3,1])) # result = 7
print(s.findLBSLength([1,3,6,7,9,4,10,5,6,2])) # result = 6
print(s.findLBSLength([1,3,6,7,9,4,10,5,6,2,1])) # result = 7
