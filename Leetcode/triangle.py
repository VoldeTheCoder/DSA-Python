class Solution:
    def minimumTotal(self, triangle):
        i_sum = {}
        def bfs(h,i):
            if h == len(triangle) - 1:
                return triangle[h][i]
            if (h, i) in i_sum:
                return i_sum[(h, i)]
            i_sum[(h, i)] = triangle[h][i] + min(bfs(h+1, i), bfs(h+1, i+1))
            return triangle[h][i] + min(bfs(h+1, i), bfs(h+1, i+1))
        return bfs(0, 0)
    
triangle = [[-1],[2,3],[1,-1,-3]]
s = Solution()
print(s.minimumTotal(triangle))