import math

class Solution:
    def countMinJumps(self, jumps):
        memo = {}
        def dfs(i = 0):
            memo_key = i
            if i == len(jumps) - 1:
                return 0
            if i >= len(jumps):
                return math.inf
            if memo_key in memo:
                return memo.get(memo_key)
            
            current_possible_jump_count = jumps[i]
            min_jump_count = math.inf
            for j in range(current_possible_jump_count, 0, -1):
                current_jump = dfs(i + j) + 1
                min_jump_count = min(min_jump_count, current_jump)

            memo[memo_key] = min_jump_count
            
            return min_jump_count



        return dfs(0)



s = Solution()
print(s.countMinJumps([2,1,1,1,4]))