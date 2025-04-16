class Solution:
    def minCut(self, s: str) -> int:
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return left, right
        
        def dfs(s = s):
            pivot = len(s) // 2
            palindrome_i, palindrome_j = 0, 0
            if len(s) % 2 == 0:
                palindrome_i, palindrome_j = expand_from_center(pivot - 1, pivot)
            else:
                palindrome_i, palindrome_j = expand_from_center(pivot, pivot)

            palindrome_length = palindrome_j - palindrome_i - 1

            if palindrome_length == len(s):
                return 0
            
            first_half = dfs(s[:palindrome_i]) + 1
            second_half = dfs(s[palindrome_j + 1:]) + 1

            return first_half + second_half
        
        return dfs(s)

s = Solution()
print(s.minCut('abbab'))


            


        