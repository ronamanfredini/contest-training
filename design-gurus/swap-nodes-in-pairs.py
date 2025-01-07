class Node:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next


class Solution:
    def swapPairs(self, head: Node) -> Node:
        def swap(head: Node, headToSwap: Node):
            if not headToSwap:
                return head
            if not headToSwap.next:
                headToSwap.next = head
                head.next = None
                return headToSwap
            
            tmp = headToSwap.next
            headToSwap.next = head
            head.next = swap(tmp, tmp.next)

            return headToSwap

        swapped = swap(head, head.next)
        return swapped


s = Solution()
node = Node(1, Node(2, Node(3, Node(4))))

print(s.swapPairs(node))