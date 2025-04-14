class Solution:
    def findLPSLength(self, st):
        memo = {}
        def is_palindrome(s):
            right = len(s) -1
            left = 0
            while left <= right:
                if s[right] != s[left]:
                    return False
                right -= 1
                left += 1
            
            return True

        def find_biggest_palindrome(string):
            if len(string) <= 0:
                return 0

            if len(string) == 1:
                return 1
            
            if string in memo:
                return memo.get(string)
            
            if is_palindrome(string):
                return len(string)

            biggest_palindrome = 1
            for i in range(len(string)):
                next_str = ('' if i == 0 else string[:i]) + string[i + 1:]
                biggest_palindrome = max(find_biggest_palindrome(next_str), biggest_palindrome)
            
            memo[string] = biggest_palindrome

            return biggest_palindrome

        return find_biggest_palindrome(st)
    

s = Solution()
print(s.findLPSLength('abdbca'))
