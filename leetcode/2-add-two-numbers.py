# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_num(self, head):
        stack = ''
        while head:
            stack += str(head.val)
            head = head.next
        
        return int(stack[::-1])

    def create_linked_list(self, arr):
        item = arr.pop()
        first_head = ListNode(int(item))
        head = first_head
        while len(arr) > 0:
            item = arr.pop()
            head.next = ListNode(int(item))
            head = head.next

        return first_head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.get_num(l1)
        num2 = self.get_num(l2)

        result = list(str(num1 + num2))
        
        return self.create_linked_list(result)





        