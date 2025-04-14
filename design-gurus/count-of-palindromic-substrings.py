class Solution:
    def findCPS(self, st):
        def is_palindrome(i1, j2):
            left = i1
            right = j2
            while left <= right:
                if st[left] != st[right]:
                    return False
                
                left += 1
                right -= 1
                
            return True

        memo = {}
        def dfs(i, j):
            length = len(st[i: j + 1])
            if length <= 0 or memo.get((i, j), False):
                return 0
            
            curr_palindrome = 1 if is_palindrome(i, j) else 0
            memo[(i, j)] = True
            remove_last_path = dfs(i, j -1)
            remove_first_path = dfs(i + 1, j)

            result = remove_last_path + remove_first_path + curr_palindrome

            return result
        res = dfs(0, len(st) - 1)

        return res


s = Solution()
print(s.findCPS('abdbca'))