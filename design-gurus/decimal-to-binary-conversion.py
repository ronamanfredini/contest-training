class Solution:
    def decimalToBinary(self, num):
        stack = []  # Create an empty stack to hold binary digits.
        while num > 0:  # Continue the loop until num becomes 0.
            stack.append(num % 2)  # Push the remainder of num divided by 2 onto the stack.
            num //= 2  # Update num by integer division (floor division) by 2.
        return ''.join(str(i) for i in reversed(stack))  # Convert the stack to a binary string.

# Test cases
sol = Solution()
print(sol.decimalToBinary(2))    # Output: "10" (Binary representation of 2)
print(sol.decimalToBinary(7))    # Output: "111" (Binary representation of 7)
print(sol.decimalToBinary(18))   # Output: "10010" (Binary representation of 18)
