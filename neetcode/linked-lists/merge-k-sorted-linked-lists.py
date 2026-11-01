import heapq
import itertools

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
counter = itertools.count()  # Generates 0, 1, 2, ...
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        result = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, next(counter), node))

        if len(heap) == 0:
            return None
        _, _2, list_start = heap[0]
        while heap:
            _, _2, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, next(counter), node.next))
                node.next = None
            
            if len(result) > 0:
                result[-1].next = node
            
            result.append(node)

        return list_start


        