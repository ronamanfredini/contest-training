class Solution:
    def findMSIS(self, nums):
        memo = {}
        def dfs(i, last_idx = -1):
            if i >= len(nums):
                return 0
            
            memo_key = (i, last_idx)
            if memo_key in memo:
                return memo.get(memo_key)

            current_num = nums[i]
            last_num = nums[last_idx]
            skip_current = dfs(i + 1, last_idx)
            take_current = 0
            if last_idx == -1 or current_num > last_num:
                take_current = dfs(i + 1, i) + current_num
            
            result = max(skip_current, take_current)
            memo[memo_key] = result

            return result
                        
            
        return dfs(0)


s = Solution()
print(s.findMSIS([4,1,2,6,10,1,12]))