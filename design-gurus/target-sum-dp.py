class Solution:
  def findTargetSubsets(self, num, s):
    total_ways = [0]
    unique_sets = set()
    def dfs(i = 0, current_sum = 0, current_set = ''):
      
      if i >= len(num):
        if current_set not in unique_sets:
          unique_sets.add(current_set)
          if current_sum == s:
            total_ways[0] += 1
        return
        
      current_num = num[i]
      dfs(i + 1, current_sum + current_num, current_set + f'+{current_num}')
      dfs(i + 1, current_sum - current_num, current_set + f'-{current_num}')
    
    dfs()
    return total_ways[0]


s = Solution()
print(s.findTargetSubsets([1, 1, 2, 3], 1))
print(s.findTargetSubsets([1, 2, 7, 1], 9))
