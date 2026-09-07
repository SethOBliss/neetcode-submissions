class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
        for i in range(len(nums)):
            res[nums[i]]=res.get(nums[i], [])+[i]
        for i in nums:
            if target-i in nums:
                print(res)
                if target-i==i and len(res[i])>1:
                    return res[i]
                elif target-i != i:
                    return res.get(i)+res.get(target-i)