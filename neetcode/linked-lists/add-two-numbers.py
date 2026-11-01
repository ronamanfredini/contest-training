from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(l1, l2, carry = 0):
            if not l1 and not l2:
                if carry == 1:
                    return  ListNode(1)
                return None
            
            if l1 and not l2:
                if carry == 1:
                    s = l1.val + carry
                    carry = 0
                    if s >= 10:
                        s -= 10
                        carry = 1
                    return ListNode(s, dfs(l1.next, None, carry))
                return l1

            if l2 and not l1:
                if carry == 1:
                    s = l2.val + carry
                    carry = 0
                    if s >= 10:
                        s -= 10
                        carry = 1
                    return ListNode(s, dfs(None, l2.next, carry))
                return l2


            s = l1.val + l2.val + carry
            carry = 0
            if s >= 10:
                s = s - 10
                carry = 1
            new_list = ListNode(s, dfs(l1.next, l2.next, carry))

            return new_list

        return dfs(l1, l2, 0)


    
def build_list(values: List[int]) -> Optional[ListNode]:
    head = None
    for val in reversed(values):
        head = ListNode(val, head)
    return head

def list_values(head: Optional[ListNode]) -> List[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values

s = Solution()
print(list_values(s.addTwoNumbers(build_list([9, 9, 9, 9, 9, 9, 9]), build_list([9, 9, 9, 9]))))  # expected: [8, 9, 9, 9, 0, 0, 0, 1]
