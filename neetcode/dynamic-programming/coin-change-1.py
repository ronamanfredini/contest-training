class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        big_num = [1e9]
        memo = {}
        def dfs(amount: int, i: int = 0):
            if i >= len(coins):
                return big_num[0]
            
            if amount == 0:
                return 0
            
            memo_key = (i, amount)
            if memo_key in memo:
                return memo[memo_key]
            
            current_coin = coins[i]
            skip_coin = dfs(amount, i + 1)

            take_coin = big_num[0]
            if current_coin <= amount:
                take_coin = dfs(amount - current_coin, i) + 1
            
            result = min(skip_coin, take_coin)
            memo[memo_key] = result

            return result
        
        result = dfs(amount)
        if result == big_num[0]:
            return -1

        return result


s = Solution()
print(s.coinChange([1, 2, 5], 11))
