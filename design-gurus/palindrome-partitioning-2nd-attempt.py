class Solution:
    def minCut(self, s: str) -> int:
        memo = {}
        def is_palindrome(s):
            left = 0
            right = len(s) - 1
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True

        def dfs(s = s):
            if s in memo:
                return memo.get(s)
            if is_palindrome(s):
                return 0
            min_cuts = len(s) - 1
            for i in range(len(s)):
                if is_palindrome(s[:i]):
                    min_cuts = min(min_cuts, 1 + dfs(s[i + 1:]))
            
            memo[s] = min_cuts
            return min_cuts

        return dfs(s)

s = Solution()
print(s.minCut('leet'))
print(s.minCut('abbab'))
print(s.minCut('abba'))
print(s.minCut('cabba'))

# Unoptimized, takes 30s to run
print(s.minCut('apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp'))


            


        