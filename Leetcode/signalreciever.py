from heapq import *

class SignalReciever:
    def signalRecievingTime(self, times, nodes, source):
        time_pair = {
            (source, source): 0
        }
        sources = {}
        for time in times:
            time_pair[(time[0], time[1])] = time[2]
            if time[0] in sources and time[0]:
                sources[time[0]].append(time[1])
            else:
                sources[time[0]] = [time[1]]
        def bfs(source):
            time = 0
            queue = [(0,source)]
            visited = set()
            while len(queue) > 0:
                heapify(queue)
                t, temp_source = heappop(queue)
                print("Current Source:",temp_source)
                prev_time = time_pair[(source, temp_source)]
                if temp_source not in visited:
                    time = t
                if temp_source in sources:
                    for target in sources[temp_source]:
                        target_time = time_pair[(temp_source, target)] + prev_time
                        print("Time upto",target,":",target_time)
                        queue.append((target_time, target))
                        print(queue)
                        time_pair[(source, target)] = target_time
                else:
                    print(temp_source, "is one of the last nodes")
                visited.add(temp_source)
                print(visited)
                print(time)
        bfs(source)
        

times = [[1,3,2], [1,2,1], [2,4,3],[3,4,1]]
s = SignalReciever()
s.signalRecievingTime(times, 3, 1)
    
