class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        max_profit = 0
        for right in range(len(prices)):
            if right == left:
                continue
            
            max_profit = max(max_profit, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right

        return max_profit
            
            
s = Solution()
print(s.maxProfit([10,1,5,6,7,1]))
print(s.maxProfit([10,8,7,5,2]))
