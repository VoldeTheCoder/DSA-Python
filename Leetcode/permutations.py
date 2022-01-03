class Solution:
    def permutations(self, nums):
        if len(nums) == 1:
            return [[nums[0]]]
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return [[nums[0], nums[1]]]
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        
        total = []
        visited = set()
        for i in range(len(nums)):
            if nums[i] not in visited:
                new_nums = nums[:i] + nums[i+1:]
                arrangements = self.permutations(new_nums)
                for arr in arrangements:
                    arr.append(nums[i])
                    total.append(arr)
            visited.add(nums[i])
        return total
        
        
nums = [1]
s = Solution()
print(s.permutations(nums))