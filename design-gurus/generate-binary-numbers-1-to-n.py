from queue import Queue

class Solution:
    def generateBinaryNumbers(self, n):
        res = []
        for i in range(1, n + 1):
            res.append(self.convertDecimalToBinary(i))
        # ToDo: Write Your Code Here.
        return res

    def convertDecimalToBinary(self, n):
        stack = []
        while n > 0:
            stack.append(str(n % 2))
            n = n // 2
        
        stack.reverse()
        return ''.join(stack)

s = Solution()
print(s.generateBinaryNumbers(3))