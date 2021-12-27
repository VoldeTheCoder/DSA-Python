class Solution:
    def threeSum(self, nums):
        index_pair = {}
        three_sum = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s = nums[i] + nums[j]
                if s in index_pair:
                    index_pair[s].append([i, j])
                else:
                    index_pair[s] = [[i, j]]
                    
        for i in range(len(nums)):
            diff = 0 - nums[i]
            if diff in index_pair:
                for pair in range(len(index_pair[diff])):
                    if index_pair[diff][pair][0] != i and index_pair[diff][pair][1] != i:
                        new_set = sorted([nums[index_pair[diff][pair][0]], nums[index_pair[diff][pair][1]], nums[i]])
                        if new_set not in three_sum:
                            three_sum.append(new_set)
                    
        print(three_sum)
        

nums = [-1,0,1,2,-1,-4]
s = Solution()
s.threeSum(nums)