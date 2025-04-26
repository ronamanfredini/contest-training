# Unfinished - didn't pass all test cases
class Solution:
    def findLBSLength(self, nums):
        memo = {}
        def dfs(i, last_index = -1, is_going_down = False):
            if i >= len(nums):
                return 0
            
            current_number = nums[i]
            last_number = nums[last_index]

            if current_number >= last_number and is_going_down and last_index != -1:
                return 0
            memo_key = (i, last_index)
            if memo_key in memo:
                return memo.get(memo_key)
            
            skip_path = dfs(i + 1, last_index, is_going_down) 
            take_path = 0
            if (current_number > last_number and not is_going_down) or last_index == -1:
                take_path = max(dfs(i + 1, i, False) + 1)
            
            elif current_number < last_number:
                take_path = dfs(i + 1, i, True) + 1

            result = max(skip_path, take_path)
            memo[memo_key] = result
            return result
            
        return dfs(0)
    
s = Solution()
print(s.findLBSLength([4,2,3,6,10,1,12]))
print(s.findLBSLength([4,2,5,9,7,3,1]))
print(s.findLBSLength([4, 5, 3, 6, 1]))
