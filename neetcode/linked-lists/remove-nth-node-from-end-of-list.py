
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode()
        dummy.next = head

        slow = dummy
        fast = head
        while n > 0 and fast:
            fast = fast.next
            n -= 1

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


        

        
        
   


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
print(list_values(s.removeNthFromEnd(build_list([1, 2]), 2)))  # expected: [1]

