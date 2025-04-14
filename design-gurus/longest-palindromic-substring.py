class Solution:
    def findLPSLength(self, st):
        def is_palindrome(string):
            right = len(string) -1
            left = 0

            while left <= right:
                if string[left] != string[right]:
                    return False
                right -= 1
                left += 1
            
            return True

        memo = {}
        def dfs(string):
            if len(string) == 0:
                return ''

            if len(string) == 1:
                return string
            
            memo_key = string

            if memo_key in memo:
                return memo.get(memo_key)
            
            if is_palindrome(string):
                return string
            
            path_removing_first_letter = dfs(string[1:])
            path_removing_last_letter = dfs(string[:len(string) - 1])


            memo[memo_key] = path_removing_last_letter
            if len(path_removing_first_letter) > len(path_removing_last_letter):
                memo[memo_key] = path_removing_first_letter

            return memo[memo_key]

        return dfs(st)

s = Solution()
print(s.findLPSLength('abdbca'))