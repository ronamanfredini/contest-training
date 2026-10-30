from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        first_head = head
        while head:
            stack.append(head)
            head = head.next

        head = stack.pop()
        first_head = head
        while stack:
            head.next = stack.pop()
            head = head.next

        head.next = None        

        return first_head

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
print(list_values(s.reverseList(head=build_list([0, 1, 2, 3]))))