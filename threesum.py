class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j, r = i+1, len(nums)-1
            while j < r:
                three_sum = nums[i] + nums[j] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[r]])
                    j += 1
                    while nums[j] == nums[j-1] and j < r:
                        j += 1
        print(res)


nums = [-1,0,1,2,-1,-4]
s = Solution()
s.threeSum()