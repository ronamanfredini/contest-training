class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        def dfs(i=0, current_sack_profit=0, current_sack_capacity = capacity):
            # base case
            if i >= len(profits):
                return current_sack_profit

            weight = weights[i]
            profit = profits[i]
            profit_with_current_choice = 0

            # compute profit with the current choice included
            if current_sack_capacity - weight >= 0:
                profit_with_current_choice = dfs(i + 1, current_sack_profit + profit, current_sack_capacity - weight)

            # compute profit without the current choice included
            profit_without_current_choice = dfs(i + 1, current_sack_profit, current_sack_capacity)            

            return max(profit_without_current_choice, profit_with_current_choice)

        return dfs()


s = Solution()
print(s.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))  # 22
