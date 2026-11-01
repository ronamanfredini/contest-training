from typing import List, Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {}
        def dfs(head):
            if not head:
                return None
            
            if head in hm:
                return hm.get(head.val)
            
            node = Node(head.val)
            hm[head] = node
            node.next = dfs(head.next)
            node.random = dfs(head.random)

            return node


        return dfs(head)


def build_list(pairs: List[List[Optional[int]]]) -> Optional[Node]:
    nodes = [Node(val) for val, _ in pairs]
    for i, (_, random_index) in enumerate(pairs):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]
    return nodes[0] if nodes else None

def list_pairs(head: Optional[Node]) -> List[List[Optional[int]]]:
    nodes = []
    while head:
        nodes.append(head)
        head = head.next
    index_of = {id(node): i for i, node in enumerate(nodes)}
    return [[node.val, index_of[id(node.random)] if node.random else None] for node in nodes]

s = Solution()
head = build_list([[3,None],[3,0],[3,None]])
copy = s.copyRandomList(head)
print(list_pairs(copy))  # expected: [[3, None], [7, 3], [4, 0], [5, 1]]
