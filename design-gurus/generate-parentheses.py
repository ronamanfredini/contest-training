class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        solutions = set()
        def backtrack(r, l, stack_count, str):
            if stack_count < 0 or r < 0 or l < 0:
                return
            if r == 0 and l == 0 and stack_count == 0:
                solutions.add(str)
                return
            if r == 0 and l > 0:
                return
            if r > 0 and l == 0:
                if stack_count == r:
                    while stack_count > 0:
                        str += ')'
                        stack_count -= 1
                        r -= 1
                    backtrack(r, l, stack_count, str)
                return
            
            if stack_count > 0:
                backtrack(r - 1, l, stack_count - 1, str + ')')
            backtrack(r, l -1, stack_count + 1, str + '(')
        
        backtrack(n, n, 0, '')
        return list(solutions)

s = Solution()
print(s.generateParenthesis(3))
# print(s.generateParenthesis(4))
# print(s.generateParenthesis(5))