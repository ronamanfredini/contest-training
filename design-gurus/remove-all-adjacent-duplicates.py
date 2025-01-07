class Solution:
    def removeDuplicates(self, s):
        stack = []
        for char in s:
            if len(stack) > 0 and stack[-1] == char:
              while len(stack) > 0 and stack[-1] == char:
                stack.pop()
            else:
              stack.append(char)

        return ''.join(stack)

s = Solution()
print(s.removeDuplicates('abbaca'))