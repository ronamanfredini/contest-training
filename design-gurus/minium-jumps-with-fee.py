class Solution:
    # O(len(fee))
    # O(N)
    def findMinFee(self, fee):
        memo = {}
        def dfs(i):
            if i >= len(fee):
                return 0
            
            memo_key = i
            if memo_key in memo:
                return memo.get(memo_key)
            
            current_element = fee[i]
            result = min(dfs(i + 1) + current_element, dfs(i + 2) + current_element, dfs(i + 3) + current_element)
            memo[memo_key] = result

            return result
            
        return dfs(0)
    
s = Solution()
print(s.findMinFee([1,2,5,2,1,2]))