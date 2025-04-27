def expand_from_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    return left + 1, right - 1

class Solution:
    def longestPalindrome(self, s):
        longest_palindrome = ''
        
        for i in range(len(s)):
            odd_pal_l, odd_pal_r = expand_from_center(s, i, i)
            even_pal_l, even_pal_r = expand_from_center(s, i, i + 1)
            
            odd_pal_len = odd_pal_r - odd_pal_l + 1
            even_pal_len = even_pal_r - even_pal_l + 1

            if odd_pal_len >= even_pal_len:
                if odd_pal_len > len(longest_palindrome):
                    longest_palindrome = s[odd_pal_l: odd_pal_r + 1]
            else:
                if even_pal_len > len(longest_palindrome):
                    longest_palindrome = s[even_pal_l: even_pal_r + 1]

        return longest_palindrome


	

        