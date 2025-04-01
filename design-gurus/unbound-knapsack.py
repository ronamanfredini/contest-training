class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        memo = {}
        def dfs(i = 0, capacity = capacity):
            if i >= len(profits):
                return 0
            
            if capacity == 0:
                return 0
            
            memo_key = (i, capacity)
            if memo_key in memo:
                return memo.get(memo_key)

            current_element_weight = weights[i]
            current_element_profit = profits[i]

            skip_current_profit = dfs(i + 1, capacity)

            take_current_profit = 0
            if current_element_weight <= capacity:
                take_current_profit = dfs(i, capacity - current_element_weight) + current_element_profit
            
            result = max(skip_current_profit, take_current_profit)

            memo[memo_key] = result

            return result

        return dfs()

s = Solution()
print(s.solveKnapsack([15, 20, 50], [1, 2, 3], 5))