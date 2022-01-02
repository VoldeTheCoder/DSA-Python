import collections
from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times, n, k):
        sources = collections.defaultdict(list)
        
        for s,t,w in times:
            sources[s].append((w, t))
            
        time_heap = [(0, k)]
        t = 0
        visited = set()
        while time_heap:
            cur_weight, cur_source = heappop(time_heap)
            if cur_source in visited:
                continue
            t = max(t, cur_weight)
            visited.add(cur_source)
            for weight, target in sources[cur_source]:
                if target not in visited:
                    heappush(time_heap, (weight + cur_weight, target))
        return t if len(visited) == n else -1  
        
        
times = [[1,2,1],[1,3,4],[2,3,1]]
s = Solution()
print(s.networkDelayTime(times, 3, 1))