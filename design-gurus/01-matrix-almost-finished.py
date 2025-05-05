def solution(mat):
    result = [[-1 for col in range(len(mat) + 1)] for row in range(len(mat))]
    
    def dfs(i, j, visited=set()):
        if i < 0 or i >= len(mat) or j < 0 or j >= len(mat) or (i, j) in visited:
            return 1e9
        
        visited.add((i, j))
        if result[i][j] != -1:
            return result[i][j]
            
        if mat[i][j] == 0:
            result[i][j] = 0
            return 0
            
        result[i][j] = 1e9
        
        res = min(
            dfs(i+1, j),
            dfs(i-1, j),
            dfs(i, j+1),
            dfs(i, j-1)
        )
        
        result[i][j] = res + 1
        return res + 1
    
    for i in range(len(mat)):
        for j in range(len(mat)):
            if result[i][j] == -1:
                dfs(i, j)

                
    return result

print(solution([
    [1,0,1,1],
    [1,1,1,1],
    [1,1,1,0]]))

