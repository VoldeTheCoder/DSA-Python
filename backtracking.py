class BackTracking:
    def pathExist(self, board, word):
        rows, cols = len(board), len(board[0])
        path = []
        found_path = False
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                board[r][c] != word[i] or
                (r, c) in path):
                return False
            
            path.append((r, c))
            result = (dfs(r+1, c, i+1) or 
                      dfs(r-1, c, i+1) or
                      dfs(r, c+1, i+1) or
                      dfs(r, c-1, i+1))
            return result
        
        for r in range(rows):
            for c in range(cols):
                if(dfs(r, c, 0)): 
                    found_path = True
                    print(path)
                    break
        if not found_path:
            print("Path not found")    
  
  
board = [['A', 'P', 'P', 'Q'], ['B', 'R', 'L', 'T'], ['W', 'R', 'E', 'S']]
s = BackTracking()
s.pathExist(board, "APPLE")
        