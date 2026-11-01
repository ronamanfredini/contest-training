from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_list(head):
            stack = []
            if not head:
                return None

            while head:
                stack.append(head)
                head = head.next
            
            init = stack.pop()
            begin = init
            while stack:
                init.next = stack.pop()
                init = init.next
            
            init.next =  None
            return begin
        


        counter = 1
        dummy = ListNode(0, head)
        group_init = dummy

        while head:
            if counter == k:
                temp = head.next
                head.next = None
                group_init.next = reverse_list(group_init.next)
                head.next = temp

                counter = 0
                group_init = head
            counter += 1
            head = head.next

        return dummy.next

def build_list(values: List[int]) -> Optional[ListNode]:
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_pylist(node: Optional[ListNode]) -> List[int]:
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5, 6])
    print(to_pylist(Solution().reverseKGroup(head, 3)))  # expected: [3, 2, 1, 6, 5, 4]
