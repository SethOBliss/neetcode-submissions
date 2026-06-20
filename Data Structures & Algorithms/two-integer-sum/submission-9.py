class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f=[]
        for i in range(len(nums)):

            if target-nums[i] in nums and nums.index(target-nums[i])!=i:
                k = nums.index(nums[i])
                j = nums.index(target-nums[i])
                if j==k:
                    j = i
                f.append(k)
                f.append(j)
                return f
