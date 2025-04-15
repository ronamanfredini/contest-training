class Solution:

    def findMinimumDeletions(self, st):
        def is_palindrome(st):
            left = 0
            right = len(st) - 1
            while left <= right:
                if st[left] != st[right]:
                    return False
                
                left += 1
                right -= 1

            return True

        memo = {}
        def dfs(st):
            if len(st) <= 0:
                return 0
            
            if is_palindrome(st):
                return 0


            memo_key = st
            if memo_key in memo:
                return memo.get(memo_key)

            result = 9999999            
            for i in range(len(st)):
                result = min(dfs(st[:i] + st[i + 1:]) + 1, result)

            memo[memo_key] = result

            return result

        return dfs(st)


s = Solution()
print(s.findMinimumDeletions('abdbca'))