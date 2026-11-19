class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        longest = s[0]
        def ex(l, r):
            if l > 0 and r < len(s) - 1 and s[l - 1] == s[r + 1]:
                return ex(l - 1, r + 1)
            
            return s[l: r + 1]


        for i in range(len(s)):
            current = s[i]
            if i + 1 < len(s) and s[i] == s[i + 1]:
                current = ex(i, i + 1)
            if len(current) > len(longest):
                longest = current
            
            current = ex(i, i)
            if len(current) > len(longest):
                longest = current



        return longest
        