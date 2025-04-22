class Solution:
    def findLISLength(self, nums):
        memo = {}
        def dfs(i, last_idx = -1):
            if i >= len(nums):
                return 0
            
            memo_key = (i, last_idx)
            if memo_key in memo:
                return memo.get(memo_key)
            
            curr_num = nums[i]
            last_num = nums[last_idx]
            skip_path = dfs(i + 1, last_idx)
            take_path = 0
            if last_idx == -1 or curr_num > last_num:
                take_path = dfs(i + 1, i) + 1

            result = max(skip_path, take_path)
            memo[memo_key] = result

            return result
        

        return dfs(0)


s = Solution()
print(s.findLISLength([4,2,3,6,10,1,12]))
print(s.findLISLength([-4,10,3,7,15]))
print(s.findLISLength([1,-4,10,]))
print(s.findLISLength([1,1,1,1,1,1,-4,10,]))
print(s.findLISLength([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-4,10,]))
print(s.findLISLength([1,3,6,7,9,4,10,5,6]))
