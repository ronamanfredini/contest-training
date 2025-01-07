class DLNode:
   def __init__(self, val=0):
       self.val = val
       self.next = None
       self.prev = None

class Solution:
    def isPalindrome(self, head):
        last_head = head
        element_count = 0
        while last_head.next:
            last_head = last_head.next
            element_count += 1
        element_count += 1

        left = 0
        right = element_count

        rightmost_head = last_head
        leftmost_head = head
        while left <= right:
            if leftmost_head.val != rightmost_head.val:
                return False
            
            left += 1
            right -= 1
            leftmost_head = leftmost_head.next
            rightmost_head = rightmost_head.prev

        return True


s = Solution()
dlNode = DLNode(1)
dlNode.next = DLNode(2)
dlNode.next.prev = dlNode
dlNode.next.next = DLNode(2)
dlNode.next.next.prev = dlNode.next
dlNode.next.next.next = DLNode(1)
dlNode.next.next.next.prev = dlNode.next.next
dlNode.next.next.next.next = None

print(s.isPalindrome(dlNode))