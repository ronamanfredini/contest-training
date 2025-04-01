class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        memo = {}
        def dfs(sack_weight, i = 0):
            if i >= len(profits):
                return 0
            
            memo_key = f'{sack_weight}-{i}'
            if memo.get(memo_key, False) != False:
                return memo.get(memo_key)
            
            curr_element_profit = profits[i]
            curr_element_weight = weights[i]

            profit1 = 0
            if sack_weight - curr_element_weight >= 0:
                profit1 = dfs(sack_weight - curr_element_weight, i + 1) + curr_element_profit

            profit2 = dfs(sack_weight, i + 1)
            result = max(profit1, profit2)
            memo[memo_key] = result

            return result

        return dfs(capacity)


s = Solution()
print(s.solveKnapsack([1,6,10,16], [1,2,3,5], 7))