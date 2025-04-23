# Goal is to make the biggest increasing sequence
# Get the deletions can be basically length of biggest sequence - length of input array

class Solution:
    def findMinimumDeletions(self, nums):
        memo = {}
        def dfs(i, last_idx = -1):
            if i >= len(nums):
                return 0
            
            memo_key = (i, last_idx)
            if memo_key in memo:
                return memo.get(memo_key)

            current_num = nums[i]
            last_num = nums[last_idx]
            skip_current_path = dfs(i + 1, last_idx)

            take_current_path = 0
            if current_num > last_num or last_idx == -1:
                take_current_path = dfs(i + 1, i) + 1

            result = max(skip_current_path, take_current_path)
            memo[memo_key] = result

            return result

        return len(nums) - dfs(0)


s = Solution()
print(s.findMinimumDeletions([4,2,3,6,10,1,12]))