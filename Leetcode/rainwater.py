def trap(height):
    volm = {}

    def dfs(start, i, vol):
        if i+1 < len(height):
            if height[i+1] < height[i]:
                return dfs(start, i+1, vol)
            else:
                if height[i+1] < height[start]:
                    j = i
                    tmp = 0
                    while j > start and height[j] < height[i+1]:
                        if j in volm:
                            vol -= volm[j]
                            volm[j] = 0 
                        tmp += height[i+1] - height[j]
                        j -= 1
                    volm[i+1] = tmp
                    return dfs(start, i+1, vol + tmp)
                else:
                    j = start
                    tmp, prev = 0, 0
                    while j < i + 1:
                        if j in volm:
                            vol -= volm[j]
                        tmp += height[start] - height[j]
                        j += 1
                    return dfs(i+1, i+1, vol + tmp)
        return vol
    return dfs(0, 0, 0)
    
height = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
print(trap(height))
