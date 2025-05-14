def sol(matrix):
    visited = set()
    island_count = 0

    def flood(i, j):
        if (i, j) in visited:
            return
        
        if i >= len(matrix) or i < 0 or j >= len(matrix[i]) or j < 0:
            return
        
        if matrix[i][j] == '0':
            return
        
        visited.add((i, j))

        flood(i + 1, j)
        flood(i - 1, j)
        flood(i, j + 1)
        flood(i, j - 1)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '1' and (i, j) not in visited:
                island_count += 1
                flood(i, j)

    return island_count



print(sol([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]))