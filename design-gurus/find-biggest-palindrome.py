class Solution:
    def find_bigggest_palindrome(self, st):
        def expand_from_center(left, right):
            while left >= 0 and right < len(st) and st[left] == st[right]:
                left -= 1
                right += 1

            return right - left - 1
    
        biggest_palindrome = 0
        for i in range(len(st)):
            odd_len_palindrome = expand_from_center(i, i)
            even_len_palindrome = expand_from_center(i, i + 1)

            biggest_palindrome = max(odd_len_palindrome, even_len_palindrome, biggest_palindrome)
        
        return biggest_palindrome


s = Solution()
print(s.find_bigggest_palindrome('abba'))
