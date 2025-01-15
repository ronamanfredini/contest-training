from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: [[int]], start: int, end: int) -> bool:
        graph = defaultdict(list)
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)
            if node == end:
                return True
            
            for neighbor in graph.get(node, []):
                res = dfs(neighbor)
                if res:
                    return res

            return False
            
       
        return dfs(start)

s = Solution()
print(s.validPath(3, [[0,1],[1,2],[2,0]], 0, 2))