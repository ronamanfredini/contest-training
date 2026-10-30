from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        h = head
        stack = []
        while h:
            stack.append(h)
            h = h.next

        stack_len = len(stack)

        start = head

        while len(stack) >= stack_len / 2:
            temp = head.next
            stack_top = stack.pop()
            stack_top.next = temp
            head.next = stack_top
            head = stack_top.next
        head.next = None
        return start
            
            


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
head = build_list([0, 1, 2, 3, 4, 5, 6])
s.reorderList(head)
print(list_values(head))  # expected: [0, 6, 1, 5, 2, 4, 3]


