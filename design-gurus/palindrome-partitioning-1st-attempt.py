class Solution:
    def minCut(self, s: str) -> int:
        memo = {}
        def expand_from_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return left, right
        
        def dfs(s = s):
            cuts = 1e9
            if s in memo:
                return memo.get(s)
            for i in range(len(s)):
                even_palindrome_i, even_palindrome_j = expand_from_center(s, i, i + 1)
                odd_palindrome_i, odd_palindrome_j = expand_from_center(s, i, i)

                even_palindrome_length = even_palindrome_j - even_palindrome_i - 1
                odd_palindrome_length = odd_palindrome_j - odd_palindrome_i - 1

                palindrome_i, palindrome_j = even_palindrome_i, even_palindrome_j
                if odd_palindrome_length > even_palindrome_length:
                    palindrome_i, palindrome_j = odd_palindrome_i, odd_palindrome_j


                if odd_palindrome_length == len(s) or even_palindrome_length == len(s):
                    return 0
                
                first_half, second_half = 0, 0
                if palindrome_i + 1 > 0:
                    first_half = dfs(s[:palindrome_i + 1]) + 1
                
                if palindrome_j - 1 < len(s) - 1:
                    second_half = dfs(s[palindrome_j:]) + 1

                result = first_half + second_half
                cuts = min(cuts, result)

            memo[s] = cuts
            return cuts
        
        return dfs(s)

s = Solution()
print(s.minCut('leet'))
print(s.minCut('abbab'))
print(s.minCut('abba'))
print(s.minCut('cabba'))

# Unoptimized, takes 30s to run
print(s.minCut('apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp'))


            


        