# Longest increasing path in matrix
class Matrix:
    def longestIncreasingPath(self, matrix):
        path = {}
        visited = set()
        
        def isValid(row, col):
            return row >= 0 and col >=0 and row < len(matrix) and col < len(matrix[0])
        
        def neighbors(row, col):
            current = matrix[row][col]
            indices = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            return [(r, c) for r, c in indices if isValid(r, c) and matrix[r][c] > current] 
        
        def dfs(row, col):
            lengths = []
            nbrs = neighbors(row, col)
            if not nbrs:
                path[(row, col)] = 1
                return 1
            length = 1
            for (r, c) in nbrs:
                if (r, c) in visited:
                    length += path[(r, c)]
                else:
                    length += dfs(r, c) 
                lengths.append(length)
                length = 1
            path[(row, col)] = max(lengths)
            visited.add((row, col))
            return path[(row, col)] 

        max_length = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if dfs(r, c) > max_length:
                    max_length = dfs(r, c)
        return max_length


matrix = [[1]]
m = Matrix()
print(m.longestIncreasingPath(matrix))
